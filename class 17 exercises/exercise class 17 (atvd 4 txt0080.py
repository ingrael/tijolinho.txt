#exercicio 4

primeiro=int(input('primeiro termo: '))
razao=int(input('razao da pa: '))
termo=primeiro
cont=1
while cont<=10:
    print(f'{termo}', end=' ')
    termo+=razao
    cont+=1
print('fim')