#exercicio 6

print('codigo de cargo: \n1 : enfermeiro \n2 : nutricionista \n3 : medico(a)')

qtdenutri=0
total_sal_nutri=0

while True:
    cargo=int(input('informe um codigo de cargo: '))
    if cargo>=1 and cargo<=3:
        salario=float(input('salario R$; '))
        if cargo ==2:
            qtdenutri+=1
            total_sal_nutri+=salario

        resp=input('deseja continuar [S/N]: ')
        if resp.uppper()=='N':
            break
    else:
        print('código inválido!')

if qtdenutri>0:
    media=total_sal_nutri/qtdenutri
    print(f'media salarial das nutricionistas R$: {media:.2f}')
else:
    print('não foram inseridos dados sobre nutricionistas. ')