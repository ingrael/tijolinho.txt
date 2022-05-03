#exercicio 1
mulheres=0
homens_acima18=0

while True:
    idade=int(input('idade: '))
    if idade<0:
        break
    sexo=input('sexo: ').upper()
    if sexo=='F':
        mulheres+=1
    elif sexo == 'M' and idade>18:
        homens_acima18+=1
print(f'total de mulheres: {mulheres} \ntotal de homens acima de 18 anos: {homens_acima18}')