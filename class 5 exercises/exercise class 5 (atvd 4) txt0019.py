
nick=input('qual o seu nome?')
upp= nick.upper()
low= nick.lower()
flex=len(nick)-nick.count(' ')
primeiro= nick.find(' ')
print('seu nome é {}'.format(nick))
print(upp)
print(low)
print('seu nome possui {} letras ao total'.format(flex))
print('seu primeito nome possui {} letras ao total'.format(primeiro))
