"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""
from numpy import *


def errorAbs(u, v):
    ex = []
    ey = []
    for i in range(22):
        ex += [abs(round(datosC[i] - u[i], 2))]
        ey += [abs(round(datosL[i] - v[i], 2))]
    return [ex, ey]


def errorProm():
    print("a")


datosC = [30, 47.2, 70.2, 77.4, 36.3, 20.6, 18.1, 21.4, 22, 25.4,
          27.1, 40.3, 57, 76.6, 52.3, 19.5, 11.2, 7.6, 14.6, 16.2, 24.7, 0]
datosL = [4, 6.1, 9.8, 35.2, 59.4, 41.7, 19, 13, 8.3, 9.1,
          7.4, 8, 12.3, 19.5, 45.7, 51.1, 29.7, 15.8, 9.7, 10.1, 8.6, 0]
