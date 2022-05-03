#exercicio 3
somaidade=0
maioridadehomem=0
nomemaisvelho=0
mulhermenor=0
mediaidade=0

for p in range(1,5):
    nome=input('nome: ').strip()
    idade=int(input('idade: '))
    sexo=input('sexo [F/M]: ').strip().upper()
    somaidade+=idade

    if p==1 and sexo in 'M':
        maioridadehomem=idade
        nomemaisvelho=nome

    if sexo in 'M' and idade>maioridadehomem:
        maioridadehomem=idade
        nomemaisvelho=nome

    if sexo in 'F' and idade<20:
        mulhermenor+=1

mediaidade=somaidade/4

print('a media da idade do grupo é de {} anos.'.format(mediaidade))
print('o homem mais velhor tem {} anos e se chama {}.'.format(maioridadehomem, nomemaisvelho))
print('')