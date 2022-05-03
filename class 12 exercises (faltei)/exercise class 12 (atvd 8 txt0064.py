#exercicio 8
n=int(input('digite a quantidade de numeros a informar: '))

soma=0

for cont in range(n):
    num=float(input('digite um número: '))
    soma+=num # soma = soma +1
media=soma/n
print('media = {:.2f}'.format(media))