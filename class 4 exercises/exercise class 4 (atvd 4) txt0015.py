nick=input('indentifique-se: ')
sold=float(input('quantidade de imóveis vendidos: ')) *200
valuesold=float(input('valor total das vendas: ')) *0.05
cash= valuesold+sold+1500
print('seu salário é de R$ {}'.format(cash))