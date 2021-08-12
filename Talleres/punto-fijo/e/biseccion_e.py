import numpy as np
from decimal import *
import math

def f(x):
    return (x**3)-(2*x)-5


tols = [10**-8, 10**-16, 10**-32, 10**-56]

for tol in tols:

    a = 1
    b = 3
    i = 0
    m = 0
    error = abs(b - a)
    
    while(error > tol and i < 100):
        
        m = (b + a)/2
        error = abs(b - a)
        i += 1   
        if f(m) == 0:
            break

        else:

            if (f(a) * f(m) < 0):
                b = m
            if (f(b) * f(m) < 0):
                a = m

    print("El resultado es ",m,"con un error de ",error,"En",i,"Iteraciones")   
