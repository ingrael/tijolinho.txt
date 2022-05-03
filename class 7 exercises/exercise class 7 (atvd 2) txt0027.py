#exercicio 2

num = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))
num3 = int(input('digite o terceiro número: '))
maior = num

if (num2 > maior):
    maior = num2
if (num3 > maior):
    maior = num3
    print('Maior: {} '.format(maior))
    menor = num
if (num2 < menor):
    menor = num2
if (num3 < menor):
    menor = num3
    print('Menor:{} '.format(menor))