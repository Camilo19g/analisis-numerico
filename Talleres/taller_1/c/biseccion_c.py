import numpy as np
from decimal import *
import math

def f(x):
    return (x**3)-((2*x)**2)+((4*x)/3)-(8/27)


tols = [10**-8, 10**-16, 10**-32, 10**-56]

for tol in tols:

    a = 3
    b = 4

    i = 0
    m = 0
    error = abs(b - a)
    
    while(error > tol and i < 1000):
        
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
