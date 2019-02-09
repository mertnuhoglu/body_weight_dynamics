import csv
import re
import numpy

class ExcelExporter(object):
    def __init__(self, model):
        self.model = model
        self.lines = self.build_csv() # dict[var,list[csv_data_row]]
        self.current_time = -1

    def build_csv(self):
#       export simulation data as csv/excel
#       first column: variable name     levels.key
#       second column: formula 		    variables[key]
#       third column: initial value 	results.value[key][0]
#       fourth column: second value	    results.value[key][1]
        lines = {}
        lines['time_'] = ['time_','']
        for key in self.model.levels:
            line = []
            line.append(key)
            formula = convert_lookups(
                    convert_if(
                    translate_mathfunctions(
                    power_symbol_translation(
                    self.convert_stocknames(
                        self.model.variables[key])))))
            line.append("'=" + formula)
            lines[key] = line
        for key in self.model.stock_names:
            line = []
            line.append(key)
            line.append('=' + self.model.stocks[key])
            lines[key] = line
        return lines

    def add(self, key, value):
        if key == "time_":
            self.current_time = value
        if type(value) in [list, numpy.ndarray]:
            return
        if not (type(value) in [float, numpy.float64]):
            self.lines[key].append(value)
            return
        self.lines[key].append("%.15g" % value)

    def write_csv(self):
        self.lines = convert_oneletter_variable_names(self.lines)
        sorted_lines = []
        for var in self.model.levels:
            sorted_lines.append(self.lines[var])
        self.add_stocks(sorted_lines)
        writer = csv.writer(open("output_dependency.csv", "wb"))
        writer.writerows(sorted_lines)
        writer2 = csv.writer(open("output_alphabetical.csv", "wb"))
        writer2.writerows(sorted(self.lines.values()))

    def convert_stocknames(self,eqn):
# stockvar__[0] -> c
        for b in self.model.stock_bunches:
            p = re.compile(r'stockvar__\[\d+\]')
            eqn = p.subn(b.name, eqn)[0]
        return eqn

    def has_time_passed(self, t):
        return t > self.current_time

    def add_stocks(self, sorted_lines):
# stocks and 'time' variable are not included in self.model.levels.
# we need to add these variables separately   
        s2 = set([i[0] for i in self.lines.values()])
        s1 = set([i[0] for i in sorted_lines])
        missing_vars = s2-s1 # stocks and 'time'
        for var in missing_vars:
            sorted_lines.append(self.lines[deconvert_oneletter(var)])

    def add_stock_data(self, stock_data, time_data):
        for step_no,t in enumerate(time_data):
            if not self.is_time_included(t): continue
            current_stocks = stock_data[step_no]
            for i,key in enumerate(self.model.stock_names):
                self.add(key,current_stocks[i])

    def is_time_included(self, t):
        return t < 2.0

def convert_oneletter_variable_names(lines):
# ex: lines = {'c': ['c+3', 'c']}
    result = {}
    for item in lines.items():     # [('c', ['c+3', 'c'])]
        row = [convert_oneletter(term) for term in item[1]] # ['c_+3', 'c_']
        result[item[0]] = row
    return result
            
def convert_oneletter(term):
# ex: c -> c_
    p = re.compile(r'\b([a-z])\b')
    return p.subn(r'\1_',term)[0]

def deconvert_oneletter(term):
# ex: c_ -> c
    p = re.compile(r'\b([a-z])_\b')
    return p.subn(r'\1',term)[0]

def translate_mathfunctions(text):
    p = re.compile(r'\blog\b\s*(?=\()')
    return p.subn(r'ln',text)[0]
def convert_if(text):
    p = re.compile(r'(?P<then>.*)\s*\bif\b\s*\(\s*(?P<cdt>.*)\)\s+\belse\b\s+\(\s*(?P<else>.*)\)')
    return p.subn(r'if(\g<cdt>, \g<then>, \g<else>)',convert_equality_condition_in_if(text))[0]
def convert_equality_condition_in_if(text):
    p = re.compile(r'(\bif \(\s*\w+\s*)(?P<var>==)(\s*\b)')
    return p.subn(r'\1=\3',text)[0]
def power_symbol_translation(text):
    p = re.compile(r'\*\*')
    return p.subn(r'^',text)[0]

def ordered_list_as_str(aList):
# >>> x = [1,2,3]
# >>> ordered_list(x)
# [(1,2),(2,3)]
    result = []
    for (i,v) in enumerate(aList[:-1]):
        result.append((str(v),str(aList[i+1])))
    return result
def convert_lookups(lookup_eqn):
# >>> convert_lookups('[(0.0,0.0),(0.4,0.4),(0.798165,0.627193),(1.30275,0.824561),(2.0,0.95),(3.0,1.0)]')
# =CHOOSE(MATCH(__x__,{0,0.4,0.79,1.3,2,3},1),SUM(LINEST({0.0,0.4},{0.0,0.4})*{__x__,1}),SUM(LINEST({0.4,0.62},{0.4,0.79})*{__x__,1}),SUM(LINEST({0.62,0.82},{0.79,1.3})*{__x__,1}),SUM(LINEST({0.82,0.95},{1.3,2.0})*{__x__,1}),SUM(LINEST({0.95,1.0},{2.0,3.0})*{__x__,1}))
    p = re.compile(r'^(\[(\(\d+\.\d+,\d+\.\d+\)(,)?)+\])\s*$')
    m = p.search(lookup_eqn)
    if not m:
        return lookup_eqn
    result = ''
    (x_values,y_values) = extract_xy_values(lookup_eqn)
    result = 'choose(match(__x__,' + curly_braced(x_values) + ',1)'
    result = result + build_sum_linests(x_values,y_values) + ')'
    return result
def extract_xy_values(lookup_eqn):
    table = eval(lookup_eqn)
    x_values = ["%.15g" % e[0] for e in table]
    y_values = ["%.15g" % e[1] for e in table]
    return (x_values,y_values)
def build_sum_linests(x_values,y_values):
    x_pairs = ordered_list_as_str(x_values) # [(1,2),(2,3)]
    y_pairs = ordered_list_as_str(y_values) # [(4,5),(5,6)]
    zipped = zip(x_pairs,y_pairs) # [((1,2),(4,5)), ((2,3),(5,6))]
    result = ''
    for dpair in zipped:
        sum = 'sum(linest({'+dpair[1][0]+','+dpair[1][1]+'},{'+dpair[0][0]+','+dpair[0][1]+'})*{__x__,1})'
        result = result + ',' + sum
    return result
def curly_braced(x_values):
    return x_values.__str__().replace('[','{').replace(']','}')
    