# from short form model to long form:
# translate_vensim.convert(model='model_short.mdl',long2short=False)
# from long form model to short form:
# translate_vensim.convert(model='model_long.mdl',long2short=True)
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

def convert(model='model.mdl',translations='translations_joined.csv',long2short=True):
   if long2short:
      from_column, to_column = 1, 7
   else:
      from_column, to_column = 7, 1
   vensim_text = open(model).read()
   t_rows = csv.reader(open(translations,'rb'))
   t_map = dict([(r[from_column],r[to_column]) for r in t_rows])
   for from_str in t_map.keys():
      if not from_str or from_str[0] is '.':
         continue
      to_str = t_map[from_str]

      vensim_text = re.subn(r'(?i)(?<!\b )\b' + from_str + r'\b(?!\s+\b)' ,to_str,vensim_text)[0]
   open('model_translated.mdl','w').write(vensim_text)

if __name__ == '__main__':
    convert()
