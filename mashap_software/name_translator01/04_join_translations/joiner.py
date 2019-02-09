#input:
#norm p ratio,proteol,norm_p_ratio,
#norm_p_ratio,np
#output:
#norm p ratio,proteol,norm_p_ratio,,np

import csv
import re

def convert(vensimhall='translations_vensimhall_with_line_nums.csv',shortlong='translations_shortlong_names.csv'):
   sl_rows = csv.reader(open(shortlong,'rb'))
   vh_rows = csv.reader(open(vensimhall,'rb'))
   sl_map = dict([tuple(r) for r in sl_rows])
   vh_map = dict([(r[3],r) for r in vh_rows])
   rows = []
   for long in vh_map.keys():
      row = vh_map[long]
      if long in sl_map:
         short = sl_map[long] 
         row[6] = short
         row[7] = short.replace('_',' ')
      rows.append(row)
   csv.writer(open('translations_joined.csv','wb')).writerows(rows)