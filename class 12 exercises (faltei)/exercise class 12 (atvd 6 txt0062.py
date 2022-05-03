#exercicio 6
primeiro=int(input('termo: '))
razao=int(input('razão: '))

decimo=primeiro+9*razao

for c in range(primeiro, decimo+razao, razao):
    print('{}'.format(c), end='->')
print('acabou')