"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""
import numpy as np
from math import *


def emc(y, inter):
    acum = 0
    for i in range(0, len(y)):
        acum += (inter[i] - y[i])**2
    return np.sqrt(acum)/len(y)


def jaccard(g1, g2):
    gr1 = list(map(lambda i: round(i, 1), g1))
    gr2 = list(map(lambda i: round(i, 1), g2))
    interseccion = len(set(gr1).intersection(set(gr2)))
    union = len(set(gr1).union(set(gr2)))
    return np.abs(interseccion/union)
