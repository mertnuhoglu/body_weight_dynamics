#input:
#desired protox,protfrac*(TEE-GNGp- GNGf)
#output:
#desired protox,protfrac*(TEE-GNGp- GNGf),desired_protox

import re

def convert(filename='translations_in.txt'):
   file = open(filename)
   text = []
   for line in file.readlines():
      line_w_comas = put_comas(
         line.strip().lower())
      var = put_underscores(find_var(line_w_comas))
      line_wo_number, num = pop_number(line_w_comas)
      text.append(line_wo_number + ',' + var + num)
   open('translations_out.csv','w').write('\n'.join(text))
   
def put_underscores(line):
   p = re.compile(r'\b \b')
   return p.subn('_',line)[0]
def put_comas(line):
   p = re.compile(r'\t+')
   return p.subn(',',line)[0]
def find_var(line):
   p = re.compile(r'(?P<var>^(\b\w+\b *)+)')
   m = p.match(line)
   return m.group('var') if m else ''
def pop_number(line):
   # matches constant numbers to parse and then move them to the end of the line
   p = re.compile(r',[-+]?\b[0-9]+(\.[0-9]+)?\b$')
   m = p.search(line)
   num = m.group() if m else ''
   return p.subn('',line)[0].strip(), num
   
if __name__ == '__main__':
    convert()
