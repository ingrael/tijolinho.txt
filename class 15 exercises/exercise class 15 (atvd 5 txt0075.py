#exercicio 5

idade=int(input('idade: '))

maisnovo=idade
maisvelho=idade

while True:
    idade=int(input('idade: '))
    if idade<0:
        break

    if idade<maisnovo:
        maisnovo=idade
    elif idade> maisvelho:
        maisvelho=idade

media=(maisnovo+maisvelho)/2

print(f'Menor idade: {maisnovo} \nMaior idade: {maisvelho} \n Média das duas idades = {media:.2f}')