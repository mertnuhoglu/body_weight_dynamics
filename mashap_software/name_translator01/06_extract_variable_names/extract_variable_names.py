import re

def extract_variable_names(vensim_file='model.mdl'):
    file = open(vensim_file,'rb')
    text = file.read()
    p = re.compile(r'(?m)^(.*?)=')
    vars = p.findall(trim_end_of_equations(text))
    vars.sort()
    f2 = open('vars.txt','wb')
    f2.write('\n'.join(vars))
    f2.close()

   
def trim_end_of_equations(text):
    p = re.compile(r'\*{10}.+')
    m = p.search(text)
    if not m:
       return text
    return text[:m.start()]
