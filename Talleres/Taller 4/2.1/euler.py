"""
@author: David Ramirez
"""


def euler(f, x, y, h, m):
    u = []
    v = []
    for i in range(m):
        y = y + h*f(x, y)
        x = x + h
        u += [x]
        v += [y]
    return [u, v]
