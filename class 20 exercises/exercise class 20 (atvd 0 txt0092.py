'''
dias=()

print(type(dias))

print(dias[3])
'''
'''
texto='phyton'
tuple(texto)
print(texto)

lista=[1,2,3,4]
lista[2]=8
print(tuple(lista))'''
'''
lista=[3,5]
tupla=(1,2,lista)

print(tupla)

#print(tupla[2])

#print(len(tupla2))

print(tupla2.count(2))

lista=['python', 1, 2, 'java']
print(lista)'''
'''
meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
n=1
while n<4:
    mes=int(input('escolha um mêS [1-12]: 0'))
    if 1<=mes<13:
        print(f'O mês é {meses[mes-1]}')
    n+=1'''
meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

#meses.append('ingrael')

meses+=['ingrael', 'tijolinho']
print(meses)

for mes in meses:
    print(mes, end=' ')