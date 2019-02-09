from numpy import *
import pylab as p
from copy import deepcopy

def get_graph(X, t, var_names, title):
    f1 = p.figure()
    for i, var in enumerate(var_names):
        p.plot(t, X[i,:], label=var)
    p.grid()
    p.legend(loc='best')
    p.xlabel('time')
    p.ylabel('')
    p.title(title)
    return f1

def draw_graph(X, t, var_names, title, path='.'):
    get_graph(X, t, var_names, title).savefig(path)