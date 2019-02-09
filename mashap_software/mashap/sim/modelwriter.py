from palamut import models
from sim.converter import Converter
import re

class ModelWriter(object):
    def __init__(self, model):
        self.model = model
        
    def get_equations_unordered(self):
        var_eqns = [name + ' = ' + self.model.variables[name] for name in self.model.variables.keys()]
        rate_eqns = [name + ' = ' + self.model.rates[name] for name in self.model.rates.keys()]
        sf_eqns = [name + ' = ' + self.model.stocks[name] for name in self.model.stocks.keys()]
        eqns = []
        eqns += var_eqns
        eqns += rate_eqns
        eqns += sf_eqns
        return eqns

    def get_unknown_functions(self, eqns):
        p = re.compile(r'\b(?=\D)\w+\s*(?=\()') # ex: "pulse(0,4)"
        return [p.findall(e) for e in eqns if p.search(e)]

    def write_stocks(self):
        out = open('eqns_stocks.txt', 'w')
        out.write("\n".join(self.model.eqns_stocks))
        out.close( )

    def write_eqns_scipy(self):
        out = open('eqns_scipy.txt', 'w')
        out.write("\n".join(self.model.eqns_scipy))
        out.close( )

    def write_eqns_sorted(self):
        out = open('eqns_readable.txt', 'w')
        out.write("\n".join(self.model.eqns_sorted))
        out.close( )

    def write_eqns_unordered(self):
        eqns = self.get_equations_unordered()

        out = open('eqns_unordered.txt', 'w')
        out.write('\n'.join(eqns))
        out.close( )

        unknown_functions = get_unknown_functions(eqns)
        if self.unknown_functions:
            out = open('unknown_functions.txt', 'w')
            out.write(self.unknown_functions.__str__())
            out.close()

    def write_eqns_matlab(self):
        converter = Converter(self.model)
        equations_matlab = open('eqns_matlab.txt', 'w')
        equations_matlab.write("\n".join(converter.matlab_eqns))
        equations_matlab.close( )

    def write_stock_inits(self):
        init_eqns = [s + ' = ' + str(self.model.stock_inits[s]) for s in self.model.stock_inits.keys()]
        out = open('stock_inits.txt', 'w')
        out.write('\n'.join(init_eqns))
        out.close()