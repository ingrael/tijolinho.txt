#exercicio 7
salário=float(input('digite seu salário: '))
cargo=input('qual seu cargo? ')
programador=float(input('seu salário é de R$ {:.2f}'.format(salário+(salário*0.3))))
analistadesistemas=float(input('seu salário é de R$ {:.2F}'.format(salário+(salário*0.2))))
analistadebancodedados=float(input('seu salário é de R$ {:.2F}'.format(salário+(salário*0.15))))
print('seu novo salário é de R$ {}'.format(cargo))