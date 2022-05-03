#exercicio 2

velocidade = float(input('qual é a velocidade atual do carro? '))

if velocidade > 80:
    print('voce foi multado! ultrapassar o limite de velocidade!')
    multa = (velocidade-80)*7
    print('voce deve pagar uma multa de R${:.2F}'.format(multa))
else:
    print('tenha um bom dia')