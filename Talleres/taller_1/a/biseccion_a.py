import numpy as np
import matplotlib.pyplot as plt
from decimal import *


def f(x):
    return (np.cos(x)*np.cos(x)) - x**2


tols = [10**-8, 10**-16, 10**-32, 10**-56]
errs = []

for tol in tols:
    errs.clear()
    a = 0
    b = 2
    i = 0
    m = 0
    err = abs(b - a)
    while(err > tol and i < 100):
        m = (b + a)/2
        err = abs(b - a)
        errs.append(err)
        i += 1
        if f(m) == 0:
            break

        else:

            if (f(a) * f(m) < 0):
                b = m
            if (f(b) * f(m) < 0):
                a = m
    plt.figure()
    plt.title("Biseccion a " + str(tol) + " de tolerancia")
    plt.xlabel("iteraciones")
    plt.ylabel("error")
    plt.plot(range(0, i), errs)
    plt.show()
    plt.savefig("grafica_biseccion_" + str(tol))
    print(
        f'Los valores de la raiz son {m} y {m * -1}, su error es {err}, y se hicieron {i} iteraciones')
