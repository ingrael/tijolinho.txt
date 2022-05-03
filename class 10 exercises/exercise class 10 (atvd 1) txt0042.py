#exercicio 1
from datetime import date

atual= date.today().year
nascimento=int(input('ano de nascimento: '))
idade=atual -  nascimento
print('o atlteta tem {} anos'.format(idade))

if idade <=9:
    print('classificação: MIRIM')
elif idade <=14:
    print('classficação: INFANTIL')
elif idade <=19:
    print('classficação: JUNIOR')
elif idade <=25:
    print('classficação: SENIOR')
else:
    print('classificação: MASTER')