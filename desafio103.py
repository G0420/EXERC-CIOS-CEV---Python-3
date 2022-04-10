def linha():
    print('='*30)

def cadastro(nomes='<desconhecido>', gol=0):
    print(f'O(A) jogador(a) {nomes} marcou {gol} gol(s) ao todo.')

linha()
nome=str(input('Nome do(a) jogador(a): '))
g=str(input('Número de gols: '))
if g.isnumeric():
    g=int(g)
else:
    g=0
if nome.strip() == '':
    cadastro(gol=g)
else:
    cadastro(nome,g)

