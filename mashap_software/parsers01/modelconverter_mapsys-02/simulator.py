from model import Model
from copy import deepcopy
from bunch import Bunch
import re
from numpy import *

class Simulator(object):
    def __init__(self, model):
        self.model = model
        self.eqns = self.build_scipy_model()

    def simulate(self):
        t = linspace(0, 180,  3600)
        from scipy import integrate
        X0 = array([10125, 500, 7500, 0])
        X = integrate.odeint(self.dX_dt, X0, t)
        return X

    def dX_dt(self, X, t=0):
        eqns_sorted = [var + ' = ' + self.eqns[var] for var in self.model.levels]
        for eqn in eqns_sorted:
            exec(eqn)
        differentials = [self.model.stocks[b.name] for b in self.stock_bunches]
        return array( [eval(diff) for diff in differentials] )
    
    def build_scipy_model(self):
        stocks = sorted(self.model.stocks.keys())
        self.stock_bunches = [Bunch(name=s, pattern=r'\b%s\b'%s, replace=r'X[%d]' % stocks.index(s)) for s in stocks]
        eqns = {}
        eqns.update( deepcopy(self.model.variables) )
        eqns.update( deepcopy(self.model.rates) )
        self.eqns = dict( [(k, self.replace(v)) for (k,v) in eqns.items()] )
        return self.eqns
    
    def replace(self, eqn):
        for b in self.stock_bunches:
            p = re.compile(b.pattern)
            eqn,n = p.subn(b.replace, eqn)
        return eqn