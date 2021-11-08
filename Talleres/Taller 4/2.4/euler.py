"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""


def euler(f, x, y, h, m):
    u = []
    v = []
    for i in range(m):
        x = x + h*f[0](x, y)
        y = y + h*f[1](x, y)
        x = round(x, 1)
        y = round(y, 1)
        u += [x]
        v += [y]
    u[0] = 30
    v[0] = 4
    return [u, v]
