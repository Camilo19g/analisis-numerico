"""
@author: Andres Malagon, Camilo Garcia, David Ramirez.
"""
from sympy import *


def lagrange(x, y, u=None):
    n = len(x)
    t = Symbol('t')
    p = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if j != i:
                L = L * (t - x[j]) / (x[i] - x[j])
        p = p + y[i] * L
        p = expand(p)
    if u == None:
        return p
    else:
        r = p.subs(t, u)
        return r
