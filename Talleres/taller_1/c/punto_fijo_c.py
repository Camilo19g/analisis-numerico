import numpy as np


def g(x):
    return (x**3)-((2*x)**2)+((4*x)/3)-(8/27)


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
