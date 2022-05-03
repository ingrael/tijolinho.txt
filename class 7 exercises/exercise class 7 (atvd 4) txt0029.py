#exercicio 4

distancia = float(input('qual a distancia da sua viagem? '))
preco=distancia*0.5 if distancia<=200 else distancia*0.45
print('e o preço da sua passagem sera de R${:.2f}'.format(preco))