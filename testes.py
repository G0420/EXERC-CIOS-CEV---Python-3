''''def linha():
    print('='*30)

def par(n=0):
    if n%2==0:
        return True
    else:
        return False
num=int(input('Digite um número: '))
if par(num)==False:
    print(f'O número {num} é ÍMPAR!')
else:
    print(f'O número {num} é PAR!')'''

import uteis
num=int(input('Digite um valor >> '))
print(f'O fatorial de {num} é {uteis.fatorial(num)}.')
