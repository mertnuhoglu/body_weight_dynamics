import re
from palamut.models import ModelDefinition

class Converter(object):
    def __init__(self, model):
        self.matlab_eqns = [self.convert_to_matlab(e) for e in model.eqns_sorted]
    
    def convert_to_matlab(self, eqn):
        return self.remove_select(
            self.extract_select_for_t0(eqn)
            )
    
    def extract_select_for_t0(self, eqn):
        # select([0.0 <= t < 84.0],[1])*1826.0 => 1*1826.0
        p = re.compile(r'select\(\[\s*0\.0\s*<=\s*t\s*<\s*\d+(\.\d+)?\s*\]\s*,\s*\[(?P<val>.*?)\]\s*\)')
        return p.subn(r'\g<val>', eqn)[0]
    
    def remove_select(self, eqn):
        # remove all select terms
        p = re.compile(r'select\(.+?\)')
        return p.subn('0', eqn)[0]