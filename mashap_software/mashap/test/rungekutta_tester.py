from numpy import array, zeros
from printSoln import *
import sim.run_kut4

def F(t,X):
   F = zeros(2)
   F[0] = X[1]
   F[1] = t
   return F

def run():
   t = 0.0
   tStop = 5
   x0 = array([0.0,1.0])
   h = 0.25
   freq = 1
   t,X = sim.run_kut4.integrate(F, t, x0, tStop, h)
   printSoln(t,X,freq)
   return t, X
