#exercicio 2
num = cont = soma = 0

num=int(input('digite um numero ou 999 para parar: '))

while num!=999:
    soma+=num
    cont+=1
    num=int(input('digite um numero ou 999 para parar: '))
print('voce digitou {} númeroa e a soma entre eles')