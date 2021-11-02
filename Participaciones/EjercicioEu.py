import numpy as np

#Función
dy = lambda x,y:  ((0.7*y) -(x**2)+1)

#Inicialización

xi = 1; xf = 2;  h = 0.01
n = 100
x = 1; y = 1

print ('x  \t\t y'); print ('%f  \t %f' % (x, y))


#Metodo Euler
for i in range (1, n+1):
  
    y = y +dy(x, y)*h
    x = x + h
    print ('%f \t %f'% (x, y))

