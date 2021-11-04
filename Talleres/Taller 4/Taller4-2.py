"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""
from euler import *
from matplotlib.pyplot import *
import math


def f(a, y):
    return (-1 * a) * y


m = 100
a0 = 0
y0 = 1
h = 0.1

[u, v] = euler(f, a0, y0, h, m)
plot(u, v, "b")
title("Solución numerica método Euler")
xlabel("α")
ylabel("y")
show()