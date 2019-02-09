import modelparser
from model import Model
import copy
from bunch import Bunch
import re
from simulator import Simulator

def test():
    reload(modelparser)
    m = modelparser.ModelParser()
    model = m.model
    sim = Simulator(model)
    return sim

def dX_dt(X, t=0):
    eqns, stock_bunches = build_scipy_model(model)
    eqns_sorted = [var + ' = ' + eqns[var] for var in model.levels]
    for eqn in eqns_sorted:
        exec(eqn)
    differentials = [model.stocks[b.name] for b in stock_bunches]
    return array( [eval(diff) for diff in differentials] )

def build_scipy_model(model):
    stocks = sorted(model.stocks.keys())
    stock_bunches = [Bunch(name=s, pattern=r'\b%s\b'%s, replace=r'X[%d]' % stocks.index(s)) for s in stocks]
    eqns = {}
    eqns.update( copy.deepcopy(model.variables) )
    eqns.update( copy.deepcopy(model.rates) )
    eqns = dict( [(k, replace(stock_bunches, v)) for (k,v) in eqns.items()] )
    return (eqns, stock_bunches)

def replace(stock_bunches, eqn):
    for b in stock_bunches:
        p = re.compile(b.pattern)
        eqn,n = p.subn(b.replace, eqn)
    return eqn