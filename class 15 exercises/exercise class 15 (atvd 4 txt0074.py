#exercicio 4
soma=0

nome = input('nadador 1: ')
tempo = float(input('tempo do nadador 1: '))

melhornadador=nome
melhortempo=tempo
piornadador=nome
piortempo=tempo

somatempo=0
soma+=tempo
tempo12s15s=0

if 12 <= tempo <=15:
    tempo12s15s+=1

for nadador in range(2,8):
    nome = input(f'nadador {nadador}: ')
    tempo = float(input(f'tempo do nadador {nadador}: '))

    if tempo<melhortempo:
        melhornadador=nome
        melhortempo=tempo
    elif tempo>piortempo:
        piornadador=nome
        piortempo=tempo

    somatempo+=tempo

    if 12 <= tempo <=15:
        tempo12s15s+=1

print(f'{melhornadador} é o melhor nadador com {melhortempo} seg. \n{piornadador} é o pior nadador com {piortempo} seg. ')

media=somatempo/7

print(f'média dos tempos = {media:.2f} seg. \n atletas entre 12 seg e 15 seg: {tempo12s15s}')