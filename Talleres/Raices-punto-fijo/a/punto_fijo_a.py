import numpy as np
from decimal import *


def f(x):
    return (np.cos(x)*np.cos(x)) - x*2


def g(x):
    return np.cos(x)


tols = [10**-8, 10**-16, 10**-32, 10**-56]
for tol in tols:
    i = 0
    x = 0
    err = np.abs(g(x) - x)
    while(err > tol and i < 1000):
        if i > 0:
            err = np.abs(g(x) - x)
        x = g(x)
        i += 1
    print(
        f'Se obtuvieron las raices {Decimal(x)} y {Decimal(x * -1)} en {i} iteraciones, error {err}')
