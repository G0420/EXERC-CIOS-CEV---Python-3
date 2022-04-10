galera=[]
dado=[]
totmaior=totmenor=0
for c in range (0,6):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    print('='*18)
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1]>=18:
        print(f'O {p[0]} é MAIOR de idade!')
        totmaior+=1
    else:
        print(f'O {p[0]} é MENOR de idade!')
        totmenor+=1
print(f'Dentre os números digitados temos {totmaior} maior(es) de idade e {totmenor} menor(es).')