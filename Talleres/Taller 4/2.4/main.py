"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""
from numpy import *
from euler import *
from error import *
from datos import *
from matplotlib.pyplot import *


def dxdt(x, y):
    # Funcion x'(t) = 0.4x(t)-0.018x(t)y(t)
    return (0.4 * x) - 0.018 * x * y


def dydt(x, y):
    # Funcion x'(t) = -0.8x(t)+0.023x(t)y(t)
    return ((-1 * 0.8) * y) + 0.023 * x * y


f = [dxdt, dydt]
x0 = 30  # x(0) = 30
y0 = 4  # y(0) = 4
h = 1
m = 22
tiempo = range(0, 22)

# Solucion Euler
[u, v] = euler(f, x0, y0, h, m)

# Errores
[eC, eL] = [errorAbs(u, getConejos()), errorAbs(v, getLinces())]


# Salida
print(
    f"🟢 El error promedio para la poblacion de conejos es: {round(average(eC), 2)}")
print(
    f"🟢 El error promedio para la poblacion de linces es: {round(average(eL), 2)}")
plot(tiempo, u, "b")
plot(tiempo, getConejos(), "ob--")
plot(tiempo, v, "r")
plot(tiempo, getLinces(), "or--")
title("Solucion con método de Euler")
xlabel("Tiempo")
ylabel("Especies")
legend(["Aprox. Conejos", "Datos Conejos",
       "Aprox. Linces", "Datos Linces"])
show()
