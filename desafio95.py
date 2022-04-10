dic={}
lista=[]
partidas=[]

print('=====CADASTRO DE JOGADORES=====')

while True:
    dic.clear()
    dic['nome']=str(input('Digite o nome do jogador: '))
    tot=int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    partidas.clear()
    for d in range (0,tot):
        partidas.append(int(input(f'Quantos gols ele fez na partida {d+1}?')))
    dic['gols']=partidas[:]
    dic['total']= sum(partidas)
    lista.append(dic.copy())

    while True:
        ask=str(input('Quer continuar? [S/N] ')) .upper()[0]
        if ask in 'SN':
            break
        print('ERRO! Digite somente S ou N.')
    if ask=='N':
        break

print('*'*30)
print('cod ',end='')
for i in dic.keys():
    print(f'{i:<15}',end='')
print()
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('*'*30)

while True:
    busca=int(input('Mostrar dados de qual jogador? '))
    if busca==999:
        print('Encerrando programa...')
        break
    if busca>=len(lista):
        print('ERRO! NÃO EXISTE JOGADOR COM O CÓDIGO DA BUSCA.')
    else:
        print(f'---LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gol(s)')