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

def convert(model='model.mdl',translations='translations.csv'):
   text = open(model).read()
   t_rows = csv.reader(open(translations,'rb'))
   t_map = dict([(r[0],r[1]) for r in t_rows])
   for from_str in t_map.keys():
      if not from_str or from_str[0] is '.':
         continue
      if t_map[from_str] is '':
         to_str = from_str
      else:
         to_str = t_map[from_str]

      text = re.subn(r'(?i)(?<!\b )\b' + from_str + r'\b(?!\s+\b)' ,to_str,text)[0]
   open('model_translated.mdl','w').write(text)

if __name__ == '__main__':
    convert()
