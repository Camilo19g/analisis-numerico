from scipy.optimize import root_scalar
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (x*np.sin(x))-1


x = np.linspace(start=-1, stop=2)
plt.plot(x, f(x))
plt.grid()
plt.savefig("graph")

try:
    sol = root_scalar(f, method='brentq', bracket=[-1, 2])
    print(f"Metodo de Brent: \n\
    - Raiz: {sol.root} \n\
    - Iteraciones: {sol.iterations}")
except:
    print("🔴 No converge")