import numpy as np
import math


def g(x):
    return ((68.1*9.81)/x)*(1-math.e**(-0.146843*x))-40


tols = [10**-8, 10**-16, 10**-32, 10**-56]

for tol in tols:
    x = 0.7
    x1 = g(x)
    err = abs(x1 - x)
    x2 = g(x1)
    err = abs(x2 - x1)
    x3 = x - ((x1 - x)**2) / (x2 - 2*x1 + x)
    err = abs(x3 - x2)
    i = 3
    while err > tol:
        x = x3
        x1 = g(x)
        err = abs(x1 - x)
        x2 = g(x1)
        err = abs(x2 - x1)
        if((x2 - 2*x1 + x) != 0):
            x3 = x - ((x1 - x)**2) / (x2 - 2*x1 + x)
            err = abs(x3 - x2)
        i += 3
    print(
        f'Los valores de la raiz es {x3} y {x3 * -1}, su error es {err}, y se hicieron {i} iteraciones')
