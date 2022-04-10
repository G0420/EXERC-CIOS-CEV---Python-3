lista1=[]
lista2=[]
lista3=[]
while True:
    lista1.append(int(input('Digite um valor: ')))
    resp=str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(lista1):
    if v%2==0:
        lista2.append(v)
    else:
        lista3.append(v)
print(f'Você digitou os números {lista1}')
print(f'Separei os números para você, os PARES são {lista2}')
print(f'Os ÍMPARES são {lista3}')