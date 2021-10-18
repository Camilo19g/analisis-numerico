"""
@author: Andres Malagon, Camilo Garcia, David Ramirez.
"""
from lagrange import *
from sympy import *

# Se utiliza una tabla de acumulacion de frecuencias
# para encontrar los valores que hay a continuacion.
x = [40, 50, 60, 70, 80]
f = [35, 83, 153, 193, 215]
print(f"🟢 x = {x}\n🟢 f(x) = {f}")

# En lagrange se retorna la función en modo de
# cadena y con la funcion sympify, esta cadena
# se puede utilizar como funcion.
p = lagrange(x, f)
resultado = p.subs('t', 55)
print(f"🟢 p(x) = {p}\n🟢 resultado = {resultado}")
