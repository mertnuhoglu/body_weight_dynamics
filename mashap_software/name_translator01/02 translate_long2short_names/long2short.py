#input:
#eff_of_possible_fatox,eff_fox_p
#eff_of_possible_fatox= with_lookup(...)
#output:
#eff_fox_p= with_lookup(...)

import re
import csv

def convert(eqns_file='eqns.txt',translations_file='translations_shortlong_names.csv'):
   eqns = open(eqns_file).read()
   translations_data = csv.reader(open(translations_file,'rb'))
   translations = dict([tuple(r) for r in translations_data])
   for long in translations.keys():
      short = translations[long]
      eqns = re.subn(r'\b'+long+r'\b',short,eqns)[0] if short else eqns
   eqns = prettify(eqns)
   open('short_eqns.txt','w').write(eqns)

def prettify(eqns):
   p = re.compile(r'\s*=\s*')
   return p.subn(' = ',eqns)[0]
   

if __name__ == '__main__':
    convert()
