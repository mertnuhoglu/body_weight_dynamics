#input:
#norm p ratio,proteol,norm_p_ratio,
#norm_p_ratio,np
#output:
#norm p ratio,proteol,norm_p_ratio,,np

import csv
import re

def convert(translations='translations_shortlong_names.csv',model='eqns.txt'):
   eqns = open(model).read()
   p = re.compile(r'^\w+(?=\s*=)',re.M)
   vars_vensim = set(p.findall(eqns))
   trans_rows = csv.reader(open(translations,'rb'))
   vars_trans = set([r[1] for r in trans_rows])
   new_vars = list(vars_vensim - vars_trans)
   open('translations_shortlong_changes.txt','wb').write('\n'.join(new_vars))