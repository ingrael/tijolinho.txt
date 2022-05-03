#exercicio 9
login=input('login:')
senha=int(input('senha:'))

if(login == 'tijolinho' and senha == '7355') or (login == 'tijolão' and senha == '6979'):
    print("seja bem vindo!")
else:
    print('usuario e senha incorretos')