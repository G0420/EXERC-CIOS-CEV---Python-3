from random import randint
from time import sleep
from operator import itemgetter
dado={'jogador1': randint(1,6),
      'jogador2': randint(1,6),
      'jogador3': randint(1,6),
      'jogador4': randint(1,6)}
ranking={}
for k,v in dado.items():
    print(f'    O {k} tirou {v} ')
    sleep(0.5)
print('Ranking dos jogadores: ')
ranking=sorted(dado.items(), key=itemgetter(1), reverse=True)
for c, i in enumerate(ranking):
    print(f'    {c+1}° lugar: {i[0]} com {i[1]}')
    sleep(0.5)
