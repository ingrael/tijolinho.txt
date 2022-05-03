#exercicio 3

for c in range(3,0,-1):
    senha = int(input("senha: "))
    if senha == 123456:
        print("ola, tijlolinho. seja bem vindo ao nosso banco!")
        break
    elif senha != 123456:
        print("senha incorreta! voce ainda tem {} tentaiva(s).".format(c-1))
        if c==1:
            print("sua senha foi bloqueada! por favor, dirija-se a um de nossos caixas.")
            break