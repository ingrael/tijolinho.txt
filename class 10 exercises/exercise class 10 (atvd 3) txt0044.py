#exercicio 3
peso = float(input('qual é seu peso?'))
altura = float(input('qual é sua altura? (m)'))
imc=peso/(altura**2)
print ('o imc dessa pessoa é de {:.1f}'.format(imc))

if imc<18.5:
    print('voce está abaixo do peso normal') 
elif 18.5 <= imc < 25:
    print('parabéms, voce esta na faixa de peso normal')
elif 25 <= imc < 30:
    print('voce está acima do peso normal')
elif 30 <= imc <40:
    print('voce está em obesidade.')
elif imc >= 40:
    print('voce está em obesidade morbida')
