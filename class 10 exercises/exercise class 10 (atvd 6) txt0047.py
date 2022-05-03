from random import randint

itens=['pedra, papel, tesoura']
computador = randint(0,2)

print('escolha: [0] pedra, [1] papel ou [2] tesoura')
jogador=int(input('qual sua jogada:'))

print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))