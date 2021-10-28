"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez 
"""
from mas_cercana import *
from pandas import *
from xlrd import *
from matplotlib.pyplot import *
import numpy as np
from scipy.interpolate import CubicSpline, interp1d
from utilidades.errores import emc, jaccard

# Recoleccion de datos del Excel
estacion = "Itatira"
cercana = masCercano(estacion)
D1 = read_excel("data/datos.xls", sheet_name=estacion)
D2 = read_excel("data/datos.xls", sheet_name=cercana)

# Generacion de arreglos de datos
y1 = D1["Temp. Interna (ºC)"].tolist()
x1 = list(map(lambda i: i*1, range(0, len(y1))))
y2 = D2["Temp. Interna (ºC)"].tolist()
x2 = list(map(lambda i: i*1, range(0, len(y2))))

# Interpolaciones
p1 = CubicSpline(np.array(x2, dtype="float"), np.array(
    y2, dtype="float"))  # Spline cubico
p2 = interp1d(x2, y2, kind="quadratic",
              fill_value="extrapolate")  # Interpolacion cuadratica

# Validacion de datos
r1 = []
r2 = p2(x1[:len(x2)])
for i in x1[:len(x2)]:
    r1.append(float(p1(i)))

# Calculo de errores
print("🟢 Error Spline cubico")
print(f"EMC: {round(emc(y1[:len(x2)], r1), 2)}°")
print(f"Indice de Jaccard: {round(jaccard(y1[:len(x2)], r1), 2)}")
print("🟢 Error Interpolacion cuadratica")
print(f"EMC: {round(emc(y1[:len(x2)], r2), 2)}°")
print(f"Indice de Jaccard: {round(jaccard(y1[:len(x2)], r2), 2)}")

# Graficar
plot(x2, y1[:len(x2)], c="#000000")
plot(x2, r1, "r--")
title("Comparacion estación " + estacion + " con " + cercana)
xlabel("Indices esperados")
ylabel("Temperaturas")
legend([estacion, cercana])
show()
