# >>> convert_to_latex.convert(filename_eqns=filename_eqns,filename_eqns_stocks='eqns_stocks_short.txt',filename_translations=filename_translations)

import csv
import re

def convert(filename_eqns='eqns.txt',filename_eqns_stocks='eqns_stocks.txt',filename_translations='translations_names_symbols.csv',delimiter=';',join=True):
   eqns = open(filename_eqns,'rb').read()
   eqns_stocks = open(filename_eqns_stocks,'rb').read()
   eqns = eqns + '\n' + eqns_stocks
   data_translations = csv.reader(open(filename_translations,'rb'),delimiter=delimiter)
   translations = dict([(r[0],r[2]) for r in data_translations])
   for (varname,symbol) in translations.items():
      p = re.compile(r'\b'+varname+r'\b')
      eqns = p.subn(symbol,eqns)[0]
   eqns = re.subn(r'\*',r'\cdot ',eqns)[0]
   file_result = open(filename_eqns.split('.')[0] + '_latex.txt','wb')
   eqns_list = eqns.splitlines()
   eqns_list.sort()
   file_result.write('\n'.join(eqns_list))
   file_result.close()
   if join:
      join_files(filename_translations,delimiter,eqns)
      
def join_files(filename_translations,delimiter,eqns):
   data_translations = csv.reader(open(filename_translations,'rb'),delimiter=delimiter)
   translations = [list(r) for r in data_translations]
   map_short2sym = dict([(line[0],line[2]) for line in translations])
   map_short2transline = dict([(line[0],line) for line in translations])
   map_sym2eqn = dict([(eqn.split('=')[0].strip(),eqn) for eqn in eqns.splitlines()])
   for (short,symbol) in map_short2sym.items():
      try: eqn = map_sym2eqn[symbol]
      except KeyError, err: print 'unknown: ' + str(err); continue
      map_short2transline[short].append(eqn)
   tuples_short2transline = sorted(map_short2transline.items())
   lines = [v for (k,v) in tuples_short2transline]
   
   file_result = open(filename_translations.split('.')[0] + '_latex.csv','wb')
   csv.writer(file_result,delimiter=delimiter).writerows(lines)