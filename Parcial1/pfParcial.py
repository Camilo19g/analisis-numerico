import numpy as np
import matplotlib.pyplot as plt
from decimal import *


def f(x):
    return 2+(np.sin(x)) - x


def g(x):
    return 2+(np.sin(x))


tols = [10**-5]
errs = []
for tol in tols:
    errs.clear()
    i = 0
    x = 0
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
    plt.savefig("grafica_punto_fijo_parcial" + str(tol))
    print(
        f'Los valores de la raiz son {x} y {x * -1}, su error es {err}, y se hicieron {i} iteraciones')