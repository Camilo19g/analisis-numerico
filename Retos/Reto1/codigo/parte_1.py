"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""
from numpy import *
from pandas import *
from xlrd import *
from utilidades.errores import *
import random as rd
from scipy.interpolate import CubicSpline, interp1d
from matplotlib.pyplot import *

# Recoleccion datos desde Excel
DATOS = read_excel("data/datos.xls", sheet_name="Itatira")
y = DATOS["Temp. Interna (ºC)"].tolist()  # Variable y = Temperatura
x = list(map(lambda i: i*1, range(0, len(y))))  # Indices esperados

# Se separa el 70% de los datos
x70 = rd.sample(x, k=int((len(x)*0.7)))  # Indices del 70% de los datos
x70.sort()
x30 = []
y70 = []
y30 = []
for i in x70:
    y70.append(y[i])
for i in range(0, len(y)):
    if i not in x70:
        y30.append(y[i])
        x30.append(i)

# Metodos de interpolacion
p1 = CubicSpline(array(x70, dtype="float"), array(
    y70, dtype="float"))  # Spline cubico
p2 = interp1d(array(x70, dtype="float"), array(
    y70, dtype="float"), kind="quadratic", fill_value="extrapolate")  # Interpolacion cuadratica

# Validacion de datos
r70_1 = []
r30_1 = []
r70_2 = p2(x70)
r30_2 = p2(x30)

for i in x70:
    r70_1.append(float(p1(i)))
for i in x30:
    r30_1.append(float(p1(i)))

# Calculo de errores
print("🟢 Error Spline cubico")
print(f"EMC: {round(emc(y30, r30_1), 2)}°")
print(f"Indice de Jaccard: {round(jaccard(r30_1, y30), 2)}")
print("🟢 Error Interpolacion cuadratica")
print(f"EMC: {round(emc(y30, r30_2), 2)}°")
print(f"Indice de Jaccard: {round(jaccard(r30_2, y30), 2)}")

# Graficar
figure(1)
plot(x, y)
plot(x70, r70_1)
plot(x70, r70_2)
title("Comparacion con el 70% de los datos")
xlabel("Indices esperados")
ylabel("Temperaturas")
legend(["Original", "Spline cubico", "Inter. Cuadratica"])
show()
