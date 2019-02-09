# one time script
# fills all the lines in translations_shortlong_names.csv file even the short name hasn't yet been defined

from __future__ import with_statement
import csv

with open('translations_shortlong_names.csv') as f:
   data = csv.reader(f)
   data_map = dict([(r[0],r[1]) for r in data])
for d in data_map.items():
    if not d[1]:
        d[1] = d[0].replace(' ','_')
with open('translations_shortlong_names_2.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerows(list(data_map.items()))
