"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""
from numpy import *


def errorAbs(u, v):
    e = []
    for i in range(len(u) - 1):
        e += [abs(round((v[i] - u[i]) / v[i], 2))]
    return e
