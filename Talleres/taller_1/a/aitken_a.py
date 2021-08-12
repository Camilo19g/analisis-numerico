import numpy as np
import matplotlib.pyplot as plt


def g(x):
    return np.cos(x)


tols = [10**-8, 10**-16, 10**-32, 10**-56]
errs = []
ap = 0

for tol in tols:
    errs.clear()
    x = 0.7
    x1 = g(x)
    err = abs(x1 - x)
    errs.append(err)
    x2 = g(x1)
    err = abs(x2 - x1)
    errs.append(err)
    x3 = x - ((x1 - x)**2) / (x2 - 2*x1 + x)
    err = abs(x3 - x2)
    errs.append(err)
    i = 3
    while err > tol:
        x = x3
        x1 = g(x)
        err = abs(x1 - x)
        errs.append(err)
        x2 = g(x1)
        err = abs(x2 - x1)
        errs.append(err)
        if((x2 - 2*x1 + x) != 0):
            x3 = x - ((x1 - x)**2) / (x2 - 2*x1 + x)
            err = abs(x3 - x2)
            errs.append(err)
        i += 3
    plt.figure()
    plt.title("Aitken a " + str(tol) + " de tolerancia")
    plt.xlabel("iteraciones")
    plt.ylabel("error")
    plt.plot(range(0, len(errs)), errs)
    plt.show()
    plt.savefig("grafica_aitken_" + str(tol))
    print(
        f'Los valores de la raiz es {x3} y {x3 * -1}, su error es {err}, y se hicieron {i} iteraciones')
