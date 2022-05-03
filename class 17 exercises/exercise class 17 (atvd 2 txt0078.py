#exercicio 2
frase=input('digite uma frase: ').strip().upper() # apos a sopa
palavras=frase.split() #apos a sopa
junto=''.join(palavras) # aposasopa
inverso=''

for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
if inverso==junto:
    print('temos um palindromo!')
else:
    print('a frase digitada não é um palindromo!')