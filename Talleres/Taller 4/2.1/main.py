"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""
from euler import *
from numpy import *
from matplotlib.pyplot import *


a = 2  # Un valor dentro del intervalo [0, 10]
t0 = 0  # Valor inicial de t
y0 = 1  # Valor inicial de y
h = 0.1  # Cantidad para el paso
m = 100  # Numero de pasos


def dy(t, y):
    return (-1 * a) * y  # Funcion y' = -αy


def y(t):
    return y0 * exp((-1 * a) * i)  # Funcion y = y0e^-αt


# Solucion numerica
[u, v] = euler(dy, t0, y0, h, m)

# Solucion analitica
[ua, va] = [arange(t0, 10, h), []]
for i in arange(t0, 10, h):
    va.append(y(i))

# Grafica
plot(u, v, "b")
plot(ua, va, "r--")
title("Solución con método Euler")
xlabel("t")
ylabel("y")
legend(["Solucion numerica", "Solucion analitica"])
show()
