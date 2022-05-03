#exercicio 5
soma=0
for c in range(1,7):
    num=int(input('digite o {} valor: '.format(c)))
    if num%2 == 0:
        soma+=num
print('a soma dos números que voce informou {} '.format(soma))