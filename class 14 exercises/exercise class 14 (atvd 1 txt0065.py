#exercicio 1

from datetime import date
cont = 0
cont1 = 0
hoje = date.today().year
for c in range(1, 8):
    n = int(input('Ano de nascimento da {} pessoa: '.format(c)))
    if (hoje - n) >= 21:
        cont += +1
    else:
        cont1 += +1
print('Em {},{} atingiram a maioridade e {} não.'.format(hoje, cont, cont1))

