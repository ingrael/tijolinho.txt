print('## programa de emprestimo ## \n responda: 0 - não e 1- sim')
nomeneg = int(input('possui nome negativado?'))

if nomeneg == 1:
    print('não pode realizar o emprestimo.')
else:
    cartass = int(input('possui carteira assinada? '))
    if cartass == 0:
        print('não pode realizar o emprestimo')
    else:
        housesome = int(input('possui casa porpria? '))
        if housesome == 0:
            print('não pode realizar o emprestimo')
        else:
            print('concede o emprestimo')
