aluno={}
aluno['Nome']=str(input('Digite o nome do(a) aluno(a): '))
aluno['Média']=float(input(f'Digite a média de {aluno["Nome"]}: '))
if aluno["Média"]>=7.0:
    print(f'O(A) aluno(a) {aluno["Nome"]} teve média {aluno["Média"]} e está APROVADO!')
else:
    print(f'O(A) aluno(a) {aluno["Nome"]} teve média {aluno["Média"]} e está REPROVADO!')
