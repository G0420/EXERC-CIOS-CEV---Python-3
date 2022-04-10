dic={}
gols=[]
totalgol=0
print('=====CADASTRO DE JOGADORES=====')
dic['Nome']=str(input('Digite o nome do jogador: '))
dic['Jogos']=int(input('Quantas partidas ele jogou? '))
for d in range (0,dic['Jogos']):
    gols.append(int(input(f'Quantos gols ele fez na partida {d}?')))
dic['Gols']=gols[:]
dic['total']=sum(gols)
print('=-'*30)
for n in range(0,dic['Jogos']):
    print(f'    ==>Na partida {n+1} fez {[dic["Gols"][n]]} gol(s)')
print(f'Com um total de {dic["total"]} gol(s).')