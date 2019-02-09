import re
import copy

class Model(object):
    def __init__(self, variables={}, rates={}, stocks={}):
        self.variables = variables
        self.rates = rates
        self.stocks = stocks
        self.stock_equations = self.find_dependencies(self.stocks)
        self.dependencies = self.find_dependencies(self.variables)
        self.dependencies.update( self.find_dependencies(self.rates) )
        self.deps_without_stocks = self.remove_dependency_on_stock( self.dependencies, self.stocks )
        self.dependencies_with_stocks = copy.deepcopy( self.dependencies )
        self.dependencies_with_stocks.update( self.find_dependencies(self.stocks) )
        self.effects = dict([(var, self.find_dependents(self.dependencies, [var])) for (var, value) in self.dependencies.items()])
        import graph
        reload(graph)
        self.levels = graph.topological_sorting( self.deps_without_stocks, self.effects)
    
    def __str__(self):
        result = "variables:\n" + self.variables.__str__() + "\nrates:\n" + self.rates.__str__() + "\nstock flows:\n" + self.stocks.__str__()
        return result
    
    def find_dependencies(self, formulas):
        return dict([ (name, set(self.find_vars(formulas[name])) ) for name in formulas.keys() ] )
    
    def find_vars(self, formula):
        # match variables, exclude function calls and 't'
        # eg: 'max(x) + t' match: 'x' exclude 'max' 't'
        variable_name_pattern = re.compile(r'(?!\b(?=\D)\w+\s*(?=\())(?!\bt\b)\b(?=\D)\w+') 
        return variable_name_pattern.findall(formula)

    def write_dependencies(self):
        lines = [i.__str__()+'\n' for i in self.dependencies.items()]
        out = open('deps.txt', 'w')
        out.writelines(lines)
        out.close()
        
        out2 = open('stocks.txt', 'w')
        out2.writelines([i.__str__()+'\n' for i in self.stock_equations.items()])
        out2.close()
        
    def find_dependents(self, dependencies, vars):
        result = []
        for variable in vars:
            result += [name for (name, value) in dependencies.items() if variable in value]
        return set(result)

    def remove_dependency_on_stock(self, a_deps, stocks):
        deps = copy.deepcopy(a_deps)
        for stock in stocks:
            for (k,v) in deps.items():
                if stock in v:
                    deps[k].remove(stock)
        return deps
