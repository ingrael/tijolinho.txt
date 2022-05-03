from math import radians, sin, cos, tan

angulo=float(input('digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('para o angulo {} o seno é {:.2f} o cosseno é {:.2f} e a tangente é {:.2f}.'.formata(angulo, seno, cosseno, tangente))
