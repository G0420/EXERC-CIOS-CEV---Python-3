num=[]
n=[]
while True:
    num.append(str(input('Digite o nome do(a) estudante: ')))
    num.append(float(input('Digite a primeira nota: ')))
    num.append(float(input('Digite a segunda nota: ')))
    n.append(num[:])
    num.clear()
    ask=str(input('Quer continuar? [S/N] '))
    if ask in 'Nn':
        break

print(f'='*30)
print(f'{"BOLETIM":^30}')
print(f'='*30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')

for pos in range(0,len(n)):
    media=(n[pos][1]+n[pos][2])/2
    print(f'{pos:<4}{n[pos][0]:<10}{media:>8.1f}')

while True:
    per=int(input('Ver notas de qual aluno(a)? [999 Interrompe] '))
    if per==999:
        print('Finalizando...')
        print('Volte sempre <3')
        break
    mediana=(n[per][1]+n[per][2])/2
    print(f'As notas de {n[per][0]} são {n[per][1]} e {n[per][2]} com média {mediana}.')
    print('=-'*30)
