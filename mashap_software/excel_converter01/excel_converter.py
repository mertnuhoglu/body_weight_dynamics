import re
import csv

def convert(model='eqns.txt'):
   eqns = open(model,'rb').readlines()
   new_eqns = []
   for line in eqns:
      new_eqns.append(line.replace('=','\t=',1))
   open('new_eqns.csv','wb').write(''.join(new_eqns))
