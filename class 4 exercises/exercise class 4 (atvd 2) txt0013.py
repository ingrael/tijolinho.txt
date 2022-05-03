#exercicio 2

from math import sqrt

x1=float(input('digite x1:'))
y1=float(input('digite y1:'))

x2=float(input('digite x2:'))
y2=float(input('digite y2:'))

d=sqrt((x2-x1)**2+(y2-y1)**2)

print('distancia entre p1 e p2 é igual {:.2f}'.format(d))
