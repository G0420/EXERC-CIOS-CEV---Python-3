ano=2022
dados={}
dados['Nome']=str(input('Digite o nome: '))
dados['Ano']=int(input('Digite o ano de nascimento: '))
dados['CTPS']=int(input('Digite sua CTPS: [0 se não tiver!] '))
dados['Idade']=idade=ano-dados['Ano']
if dados['CTPS']==0:
    print(f'O nome é {dados["Nome"]} e tem {dados["Idade"]} anos!')
else:
    dados['Ano de contratação']=int(input('Digite o ano de contratação: '))
    dados['Salário']=int(input('Digite o salário: '))
    dados['Aposentadoria']=dados['Idade']+35
for v in dados.items():
    print(f'O(A) {v[0]} é {v[1]} ')
