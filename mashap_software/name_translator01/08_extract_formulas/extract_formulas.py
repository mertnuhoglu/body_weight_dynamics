# translate_names.convert( translations='translations_from_hall_to_modellong070604.csv', model='hall06.mdl')
# input:
#    desired carbox=
#       frac carbox * shared energy expenditure + gng fat + gng protein
#       ~	kcal/Day
#       ~		|
# output:
#    cox d =
#       fc * see + gngf + gngp
#       ~	kcal/Day
#       ~		|

import re
import csv

def extract_formulas(eqns='eqns.txt',variables='variables.txt'):
   variables = open(variables).read()
   eqns_text = open(eqns).read()
   p = re.compile(r'(?m)^\s*(?P<var>(\w+\s*)+)\s*=(?P<formula>.*?)$')
   eqns = p.findall()
   map_var_formula = {}
   for eqn in eqns:
      m = p.search(eqn)
      if m:
         map_var_formula[m.group('var')] = m.group('formula').strip()
   open('model_translated.mdl','w').write(text)

if __name__ == '__main__':
    convert()
