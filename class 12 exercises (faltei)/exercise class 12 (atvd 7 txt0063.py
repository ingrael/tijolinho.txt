#exercicio 7
sexo=input('informe seu sexo [M/F]: ').strip().upper()
while sexo not in 'MF':
    sexo=input('dados inválidos. Por favor, informe seu sexo [M/F]: ').strip().upper()
print('sexo {} registrado com sucesso.'.format(sexo))