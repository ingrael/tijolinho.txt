#exercicio 5

from ast import Num
from re import U


num = input('digite um número: ')
u=num[3]
d=num[2]
c=num[1]
m=num[0]

print('analisando o numero {}, é possível determinar que a unidade é {}, a dezena {}, a centena {} e o milhar {}.'.format(num,u,d,c,m))
