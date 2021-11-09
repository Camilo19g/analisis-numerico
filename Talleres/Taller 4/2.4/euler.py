"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""


def euler(f, x, y, h, m):
    u = []
    v = []
    for i in range(m):
        x = x + h*f[0](x, y)
        y = y + h*f[1](x, y)
        u += [round(x, 1)]
        v += [round(y, 1)]
    return [u, v]
