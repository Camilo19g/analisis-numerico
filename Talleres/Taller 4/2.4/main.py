"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""
from numpy import *
from euler import *
from error import *
from matplotlib.pyplot import *


def dxdt(x, y):
    return (0.4 * x) - 0.018 * x * y


def dydt(x, y):
    return ((-1 * 0.8) * y) + 0.023 * x * y


def imprimir(u, v, ex, ey):
    print("Año\tConejos\tLinces\tE. Conejos\tE. Linces")
    for i in range(22):
        print(f"{1900 + i}\t{u[i]}\t{v[i]}\t{ex[i]}\t{ey[i]}")


f = [dxdt, dydt]
x0 = 30
y0 = 4
h = 1
m = 22
tiempo = range(0, 22)

[u, v] = euler(f, x0, y0, h, m)
[ex, ey] = errorAbs(u, v)
imprimir(u, v, ex, ey)

plot(tiempo, u)
plot(tiempo, v)
xlabel("Tiempo")
ylabel("Especies")
show()
