#exercicio 3
resp='S'
soma=quant=media=maior=menor=0

while resp in 'S':
    num=int(input('digite um numero: '))
    soma+=num
    quant+=1
    if quant == 1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num< num:
            menor=num
    resp=input('quer continuar [S/N]? ').upper().strip()
media=soma/quant

print(f'voce digitou {quant} núemros e a média foi {media}')
print(f'voce digitou {quant} núemros e a média foi {media}')