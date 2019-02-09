from elementtree import ElementTree 
import re
from palamut.models import ModelDefinition

class ModelParser(object):
    def __init__(self, model_file=''):
        if model_file:
            self.model = self.process_file(model_file)
        else:
            self.model = self.main_file()

    def remove_malsyntax(self, eqn):
        return self.remove_new_lines(
            self.convert_pulse_to_select(
            self.convert_ints_to_floats(
            self.convert_power_operator(
            self.remove_namespaces(eqn)
            )))) 
    
    def convert_pulse_to_select(self, eqn):
        # "pulse(0,84.0)" replaced with "select([0 <= t < 84.0])"
        pattern_pulse = re.compile(r'pulse\(\s*(?P<start>\d+(\.\d+)?)\s*,\s*(?P<end>\d+(\.\d+)?)\s*\)')
        replacement_select = r'select([\g<start> <= t < \g<end>],[1])'
        return pattern_pulse.subn(replacement_select, eqn)[0]

    def remove_new_lines(self, eqn):
        p = re.compile(r'\n\s*')
        return p.subn(' ',eqn)[0]
    
    def convert_ints_to_floats(self, eqn):
        # ex match: '270' non: "0.25" '.25' '2.7'
        p = re.compile(r'\b(?!0\.\d+)(?<!\.)(\d+)\b(?!\.)') 
        return p.subn(r'\1.0', eqn)[0]
    
    def convert_power_operator(self, eqn):
        # ex match: '^'
        p = re.compile(r'\^') 
        return p.subn(r'**', eqn)[0]
    
    def remove_namespaces(self, eqn):
        p = re.compile(r'\b(?!\d+)\w+\.((\w)+)') # ex match: "main.gng_p" non: "0.25"
        return p.subn(r'\1', eqn)[0]
    
    def sum_up_flows(self, uni_inflows, bi_inflows, uni_outflows, bi_outflows):
        eqn = ""
        if uni_inflows:
            eqn += ' + ' + " + ".join(uni_inflows)
        if bi_inflows:
            eqn += ' + ' + " + ".join(bi_inflows)
        if uni_outflows:
            eqn += ' - ' + " - ".join(uni_outflows)
        if bi_outflows:
            eqn += ' - ' + " - ".join(bi_outflows)
        return eqn
    
    def process_file(self, name):
        return self.parse(ElementTree.parse(name))
    
    def process_xml_string(self, xml_string):
        return parse(ElementTree.XML(xml_string))
    
    def parse(self, tree):
        aux_nodes = tree.findall(".//auxiliary")
        variables = dict([ (e.get('text-id'), self.remove_malsyntax(e.findtext('./value')) ) for e in aux_nodes ])
        rate_nodes = tree.findall(".//rate")
        rates = dict([ (e.get('text-id'), self.remove_malsyntax(e.findtext('./value')) ) for e in rate_nodes ])
        stock_flows = dict([
            (e.get('text-id'), 
            self.remove_malsyntax(self.sum_up_flows(
                [x.text for x in e.findall('./inflows/uniflow')], 
                [x.text for x in e.findall('./inflows/biflow')], 
                [x.text for x in e.findall('./outflows/uniflow')], 
                [x.text for x in e.findall('./outflows/biflow')] ))
            ) for e in tree.findall(".//reservoir") ])
        stock_inits = dict([(e.get('text-id'),float(e.findtext('./init-value')))
            for e in tree.findall(".//reservoir")])
        model = ModelDefinition(variables, rates, stock_flows, stock_inits) # todo: bug ModelDefinition(variables, rates, stock_flows, stock_inits)
        return model

    def main_file(self):
        model = self.process_file("model.xml")
        return model