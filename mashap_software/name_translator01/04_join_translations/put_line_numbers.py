
def convert(vensimhall='translations_vensimhall.csv'):
   lines = open(vensimhall,'r').readlines()
   newlines = []
   c = 0
   for r in lines:
      newlines.append(str(c)+','+r)
      c = c + 1
   open('translations_vensimhall_with_line_nums.csv','w').write(''.join(newlines))