#exercicio 5
from random import randint

computador=randint(0,10)

print('pensei em um número de 0 a 10, tente adivinhar: ')

acetou=False
palpites=0

while not acertou:
    jogador=int(input('qual seu palpite? '))
    palpites+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador<computador:
            print('mais ... tente mais uma vez')
        