#exercicio 1

from random import randint

computador=randint(0,5)

print('vou pensar em um número entre 0 e 5')

jogador = int(input('em que numero estou pensando? '))

if jogador == computador:
    print('PARABENS VOCE ACERTOU!')
else:
    print('GANHEI, O NÚMERO NO QUAL PENSEI ERA {}, VOCE ERROU!'.format(computador))