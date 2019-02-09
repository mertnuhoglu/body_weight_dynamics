from elementtree import ElementTree 
import re

def remove_new_lines(eqns):
   return [re.sub(r'\n\s*',' ',e) for e in eqns]

def write_sf_eqns(stock_flows):
    sf_eqns = []
    for sf in stock_flows:
        eqn = 'd' + sf[0] + ' = '
        if sf[1]:
            eqn += ' + ' + " + ".join(sf[1])
        if sf[2]:
            eqn += ' + ' + " + ".join(sf[2])
        if sf[3]:
            eqn += ' - ' + " - ".join(sf[3])
        if sf[4]:
            eqn += ' - ' + " - ".join(sf[4])
        sf_eqns.append(eqn)
    return sf_eqns

def process_file(name):
    return parse(ElementTree.parse(name))

def process_xml_string(xml_string):
    return parse(ElementTree.XML(xml_string))

def parse(tree):
    aux = tree.findall(".//auxiliary")
    var_nodes = [e.get('text-id') + ' = ' + e.findtext('./value') for e in aux]
    rates = tree.findall(".//rate")
    rate_nodes = [e.get('text-id') + ' = ' + e.findtext('./value') for e in rates]
    stock_nodes = tree.findall(".//reservoir")
    stock_flows = [(
        e.get('text-id'), 
        [x.text for x in e.findall('./inflows/uniflow')], 
        [x.text for x in e.findall('./inflows/biflow')], 
        [x.text for x in e.findall('./outflows/uniflow')], 
        [x.text for x in e.findall('./outflows/biflow')]
        ) for e in stock_nodes]
    # sf_eqns = ['d' + s[0] + ' = ' + " + ".join(s[1]+s[2]) + " - ".join(s[3]+s[4]) for s in stock_flows] 
    sf_eqns = write_sf_eqns(stock_flows)
    eqns = []
    eqns += var_nodes
    eqns += rate_nodes
    eqns += sf_eqns
    return "\n".join(remove_new_lines(eqns))

def main_file():
    eqns = process_file("model.xml")
    
    out = open('out.txt', 'w')
    #out.writelines(eqns)
    out.write(eqns)
    out.close( )

