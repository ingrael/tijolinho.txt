#exercicio 2 (correção)
times=('corinthians', 'palemira', 'santos', 'gremio', 'cruzeiro', 'flamengo', 'vasco', 'chapecoense', 'atletico', 'botafogo', 'atletico-PR', 'bahia', 'são paulo', 'fluminense', 'sport recife', 'vitoria', 'coritiba', 'avai', 'ponte preta', 'atletico-GO')

print(f'cinco primeiros colocados {times[0:5]}')

print(f'quatro ultimos colocados {times[-4:]}')

times.index('chapecoense')
print(f'a chapecoense está na {times} posição')