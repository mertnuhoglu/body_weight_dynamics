# vensimparser.convert(file='model_long.mdl')

import re

def extract_stocks(text):
    stock_inits = []
    eqns_stocks = []
    eqns = []

    pattern_integ = r'(?im)^\b(?P<stock>\w+)\b\s*=\s*INTEG\b\s*\(\s*(?P<formula>.*)\b\s*,\s*\b(?P<init>\w+(\.\w+)?)\b\s*\)\s*$'
    c = re.compile(pattern_integ)
    for line in text.splitlines():
        m = c.search(line)
        if m:
            stock_inits.append(m.group('stock') + ' = ' + m.group('init'))
            eqns_stocks.append(m.group('stock') + ' = ' + m.group('formula'))
        else:
            eqns.append(line)
    return (eqns, eqns_stocks, stock_inits)

def convert(file='model.mdl'):
    text = open(file).read()
    text = format_vensim_eqns(text)
    (eqns, eqns_stocks, stock_inits) = extract_stocks(text)
    eqns.sort()
    open('eqns.txt','wb').write('\n'.join(eqns))
    open('eqns_stocks.txt','wb').write('\n'.join(eqns_stocks))
    open('stock_inits.txt','wb').write('\n'.join(stock_inits))

def temp_format(text):
    return (
            int_to_float(
            power_symbol_translation(
            translate_mathfunctions(
            ifthenelse_to_if(
            remove_backslashes(
            space_to_underscore(
            trim_from_vertical_bar(
            one_line_per_eqn(
            trim_end_of_equations(
            trim_utf8_notation(text))))))))))).strip()

def format_vensim_eqns(text):
    return convert_lookups(
            int_to_float(
            power_symbol_translation(
            translate_mathfunctions(
            ifthenelse_to_if(
            remove_backslashes(
            space_to_underscore(
            trim_from_vertical_bar(
            one_line_per_eqn(
            trim_end_of_equations(
            trim_utf8_notation(text))))))))))).strip()
def convert_lookups(text):
    # ex: eff_of_possible_fatox= with_lookup (possible_fatox / desired_fatox,([(0.0,0.0)-(3.0,1.0)],(0.0,0.0),(0.4,0.4),(0.798165,0.627193) ))
    p = re.compile(r'(?<=\],)(\(.+\d\s*\))') # (0.0,0.0),(0.4,0.4),(0.798165,0.627193)
    new_lines = []
    new_text = text
    count = 0
    for line in text.splitlines():
        m = p.search(line)
        if m:
            new_lines.extend(newlines_for_interpolation(m, line, count))
            count = count + 1
    result = remove_withlookup_lines(new_text)
    result.extend(new_lines)
    return '\n'.join(result) 
def remove_withlookup_lines(text):
    p = re.compile(r'=\s*with_lookup\s*\(') # = with_lookup (...)
    result = []
    for line in text.splitlines():
        m = p.search(line)
        if not m:
            result.append(line)
    return result
def newlines_for_interpolation(matcher, line, count):
    result = []
    lookup = matcher.group(0) # (0.0,0.0),(0.4,0.4),(0.798165,0.627193)
    varname = line.split('=',1)[0] # eff_of_possible_fatox
    table_var = 'table_' + varname # table_eff_of_possible_fatox
    result.append(table_var + ' = [' + lookup + ']') # table_eff_of_possible_fatox = [(0.0,0.0),(0.4,0.4),(0.798165,0.627193)]
    x_var = '__pts_x_' + str(count) # pts_x_0
    y_var = '__pts_y_' + str(count) # pts_y_0
    result.append(x_var + ' = array([__x for __x,__y in ' + table_var + '])') # pts_x = array([x for x,y in table_eff_of_possible_fatox])
    result.append(y_var + ' = array([__y for __x,__y in ' + table_var + '])')
    result.append(varname + ' = numpy.interp(' + find_domainvars(line) + ', ' + x_var + ', ' + y_var + ')' )# eff_of_possible_fatox = interpolate.UnivariateSpline(pts_x,pts_y)
    return result
def find_domainvars(line):
    varname = line.split('=',1)[0] # eff_of_possible_fatox
    p_domainvars = re.compile(r'(with_lookup\s*\(\s*)(?P<dom>[^,]+)') # possible_fatox / desired_fatox
    m_domainvars = p_domainvars.search(line)
    return m_domainvars.group('dom') # possible_fatox / desired_fatox

def trim_utf8_notation(text):
    p = re.compile(r'{UTF-8.*}\s*',re.I)
    m = p.search(text)
    if not m:
       return text
    return text[m.end():]
def trim_end_of_equations(text):
    p = re.compile(r'\*{10}.+')
    m = p.search(text)
    if not m:
       return text
    return text[:m.start()]
def one_line_per_eqn(text):
    p = re.compile(r'\n(?!\n)\s*')
    return p.subn('',text)[0]
def trim_from_vertical_bar(text):
    p = re.compile(r'~.*|')
    return p.subn('',text)[0]
def space_to_underscore(text):
    p = re.compile(r'\b \b')
    return p.subn('_',text)[0]
def remove_backslashes(text):
    p = re.compile(r'\\')
    return p.subn('',text)[0]
def ifthenelse_to_if(text):
    p = re.compile(r'\bIF_THEN_ELSE\b\s*\(\s*(?P<cdt>.*),\s*(?P<then>.*),\s*(?P<else>.*)\)\s*$',re.M)
    return convert_equality_condition_in_if(p.subn(r'\g<then> if (\g<cdt>) else (\g<else>)',text)[0])
def convert_equality_condition_in_if(text):
    p = re.compile(r'(\bif \(\s*\w+\s*)(?P<var>=)(\s*\b)')
    return p.subn(r'\1==\3',text)[0]
def translate_mathfunctions(text):
    p = re.compile(r'\bln\b\s*(?=\()')
    return p.subn(r'log',text.lower())[0]
def power_symbol_translation(text):
    p = re.compile(r'\^')
    return p.subn(r'**',text)[0]
def int_to_float(text):
    p = re.compile(r'(?<!\.)\b(?P<num>\d+)(?!\.\d+)\b')
    return p.subn(r'\g<num>.0',text)[0]


if __name__ == '__main__':
    convert()