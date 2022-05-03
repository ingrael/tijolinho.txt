#EXERCICIO 5
numerocamisa=int(input('numero de camisas: '))
valorcamisa = 12.5
valorfinal = numerocamisa*valorcamisa
if numerocamisa <=5:
    valorfinal=valorfinal*(1-3/100)
elif numerocamisa<=10:
    valorfinal=valorfinal*(1-5/100)
else:
    valorfinal=valorfinal*(1-7/100)

print('valor final: R$ {:.2F}'.format(valorfinal))