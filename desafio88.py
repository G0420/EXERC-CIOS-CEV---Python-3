from random import randint
from time import sleep
print('-Mega Sena-')
ask=int(input('Quantos jogos quer que eu sorteie? '))
print(f'Certo, sorteando {ask} jogos...')
sleep(1)
for n in range(0,ask):
    jogo=[]
    while len(jogo)!=6:
        num=randint(1,60)
        if num not in jogo:
            jogo.append(num)
    print(f'Jogo {n+1}: {sorted(jogo)}')
    sleep(1)
print('Boa sorte!')