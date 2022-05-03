#exercicio 1
num=(int(input('Digite um npumero:'))), int(input('digite um outro número:'))
int(input('digite mais um npumero:')), int(input('digite o ultimo número:'))

if 9 in num:
    print(f'O valor apareceu {num.count(9)} vezes')
else:
    print(f'o número 9 não foi informado.')
if 3 in num:
    print(f'O npumero 3 foi digitado na {num.index(3)+1} posição.')
else:
    print(f'o número 3 não foi informado.')

