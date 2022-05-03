#exercicio 5
total=totmil=menor=cont=0
barato=''
while True:
    produto=str('nome do produto: ')
    preco=float(input('preco R$ '))
    cont+=1
    total+=preco
    if preco>1000:
        totmil+=1
    if cont==1 or preco<menor:
        menor=preco
        barato=produto
    resp=''
    while resp not in 'SN':
        resp=input('quer continuar [S/N]?').strip().upper()
    if resp=='N':
        break
print(f'o total de compras foi R${total:.2f}')
print(f'temos {totmil} produtos custando mais de R$1000,00.')
print(f'o produto mais barato foi {produto} que custa R${menor:.2f}')