"""
@author: Andres Malagon, Camilo Garcia, David Ramirez 
"""
from numpy import *
from lagrange import *

# GRADO 3
x = [4410000, 4830000, 5250000, 5670000]
x = array(x, dtype=float)
y = [1165978, 1329190, 1501474, 1682830]
y = array(y, dtype=float)

p1 = lagrange(x, y)
r1 = p1.subs('t', 5000000)
print(f"🟢 L**3 = {p1} => {r1}")

# GRADO 2
a = [4410000, 4830000, 5250000]
a = array(a, dtype=float)
b = [1165978, 1329190, 1501474]
b = array(b, dtype=float)

p2 = lagrange(a, b)
r2 = p2.subs('t', 5000000)
print(f"🟢 L**2 = {p2} => {r2}")
