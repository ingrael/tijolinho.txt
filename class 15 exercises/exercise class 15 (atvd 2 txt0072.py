#exercicio 2

soma=0

medicamento=input('medicamento: ')
preco=float(input('R$: '))

maisbarato=medicamento
menorpreco=preco

soma+=preco

for x in range(4):
    medicamento=input('medicamentos: ')
    preco=float(input('R$: '))
    if preco<menorpreco:
        menorpreco=preco
        maisbarato=medicamento
    soma+=preco
media=soma/5

print(f'{maisbarato} é o medicamento mais barato e custa R$ {menorpreco}. \n media dos preços: {media}: ')