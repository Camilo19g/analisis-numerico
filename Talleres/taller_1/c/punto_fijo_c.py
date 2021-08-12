import numpy as np
from decimal import *


def f(x):
    return (x**3)-((2*x)**2)+((4*x)/3)-(8/27)


def g(x):
    return 1/np.sin(x)


tols = [10**-8, 10**-16, 10**-32, 10**-56]
for tol in tols:
    i = 0
    x = 0.7
    err = np.abs(g(x) - x)
    while(err > tol and i < 1000):
        if i > 0:
            err = np.abs(g(x) - x)
        x = g(x)
        i += 1
    print(
        f'Se obtuvieron las raices {Decimal(x)} y {Decimal(x * -1)} en {i} iteraciones, error {err}')
