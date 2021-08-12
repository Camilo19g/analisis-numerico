import numpy as np
import matplotlib.pyplot as plt
from decimal import *


def g(x):
    return ((2*x**2) - (4/3*x) + (8/27))**(1/3)


tols = [10**-8, 10**-16, 10**-32, 10**-56]
errs = []
for tol in tols:
    errs.clear()
    i = 0
    x = 0.7
    err = np.abs(g(x) - x)
    errs.append(err)
    while(err > tol and i < 1000):
        if i > 0:
            err = np.abs(g(x) - x)
            errs.append(err)
        x = g(x)
        i += 1
    plt.figure()
    plt.title("Punto fijo a " + str(tol) + " de tolerancia")
    plt.xlabel("iteraciones")
    plt.ylabel("error")
    plt.plot(range(0, i), errs)
    plt.show()
    plt.savefig("grafica_punto_fijo_" + str(tol))
    print(
        f'Los valores de la raiz son {x} y {x * -1}, su error es {err}, y se hicieron {i} iteraciones')
