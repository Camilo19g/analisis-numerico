

import numpy as np

#Función
dy = lambda x,y:  (np.cos(2*x)+ np.sin(3*x))

#Inicialización

xi = 0; xf = 1;  h = 0.1
n = int((xf - xi) /h)
x = 0; y = 1

print ('x  \t\t y'); print ('%f  \t %f' % (x, y))


#Metodo Euler
for i in range (1, n+1):
  
    y = y +dy(x, y)*h
    x = x + h
    print ('%f \t %f'% (x, y))

