#exercicio 4
preço=float(input('digite o valor do produto: '))
print('SIMULADOR DE VENDAS:')
print('à vista no dinheiro R$ {:.2f}'.format(preço-(preço*0.1)))
print('crédito à vista R$ {:.2f}'.format(preço-(preço*0.05)))
print('parcelado em até 2x R$ {}'.format(preço))
#resolução
preço=float(input('preço das compras: R$'))