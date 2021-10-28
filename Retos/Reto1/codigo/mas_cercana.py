"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""
from pandas import *
from numpy import *
from matplotlib.pyplot import *

# Extraemos los datos del csv de
# coordenadas.
col = ["x", "y", "Estaciones"]
COORD = read_csv("data/coordenadas.csv", names=col)
x = array(COORD.x.tolist(), dtype="float")
y = array(COORD.y.tolist(), dtype="float")
est = COORD.Estaciones.tolist()


def actual(nombre):
    for i in range(0, len(x)):
        if est[i] == nombre:
            return [x[i], y[i]]


def masCercano(nombre):
    c0 = actual(nombre)
    cercano = ""
    m = 999
    for i in range(0, len(x)):
        d = sqrt(((x[i]-c0[0])**2)+((y[i]-c0[1])**2))
        if d < m and est[i] != nombre:
            cercano = est[i]
            m = d
    print(f"🌍 {cercano} es la estacion mas cercana a {nombre}")
    return cercano
