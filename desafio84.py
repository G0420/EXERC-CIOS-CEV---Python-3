dado=[]
galera=[]
maior=menor=0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera)==0:
        maior=menor=dado[1]
    else:
        if dado[1]>maior:
            maior=dado[1]
        if dado[1]<menor:
            menor=dado[1]
    print('-='*11)
    galera.append(dado[:])
    dado.clear()
    per=str(input('Quer continuar? [S/N] '))
    if per in 'Nn':
        break

print(f'Ao todo você cadastrou um total de {len(galera)} pessoas;')
print(f'O MAIOR peso cadastrado foi {maior}kg de ',end='')
for p in galera:
    if p[1]==maior:
        print(f'{p[0]}')
print(f'O MENOR peso cadastrado foi {menor}kg de ',end='')
for p in galera:
    if p[1]==menor:
        print(f'{p[0]}')
