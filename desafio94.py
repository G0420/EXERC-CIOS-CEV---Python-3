dados={}
lista1=[]
soma=media=0
while True:
    print('=-'*20)
    dados.clear()
    dados['Nome']=str(input('Digite o nome: '))
    while True:
        dados['Sexo']=str(input('Digite o sexo: [M/F]')).upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F.')
    dados['Idade']=int(input('Digite a idade: '))
    soma+=dados['Idade']
    lista1.append(dados.copy())
    while True:
        ask=str(input('Quer cadastrar mais alguém? [S/N] ')).upper()[0]
        if ask in 'SN':
            break
        print('ERRO! por favor digite apenas S ou N.')
    if ask=='N':
        break
print('='*30)
print(f'A)> Ao todo temos {len(lista1)} pessoa(s) cadastrada(s)!')
media=soma/len(lista1)
print(f'B)> A média de idade é de {media:5.2f} anos.')

print(f'C)> As mulheres cadastradas foram: ', end='')
for p in lista1:
    if p['Sexo']=='F':
        print(f'{p["Nome"]}',end='')
print()
print(f'D)> A lista de pessoas acima da média: ')
for p in lista1:
    if p['Idade']>= media:
        print('   ',end='')
        for k, v in p.items():
            print(f' {k} = {v}',end='')
        print()
print('-FIM-')
