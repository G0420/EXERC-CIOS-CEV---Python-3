from d107 import moeda
from time import sleep
while True:
    d=float(input('Digite um preço: R$'))
    print('Carregando ', end='')
    sleep(0.5)
    print('. ',end='')
    sleep(0.5)
    print('. ',end='')
    sleep(0.5)
    print('. ',end='')
    sleep(0.5)
    print()
    print(f'A metade de {moeda.moeda(d)} é {(moeda.metade(d, True))}')
    sleep(2)
    print(f'O dobro de {moeda.moeda(d)} é {(moeda.dobro(d, True))}')
    sleep(2)
    print(f'Aumentando 10% em {moeda.moeda(d)} temos: {(moeda.aumentar(d, True))}')
    sleep(2)
    print(f'Diminuindo 13% de {moeda.moeda(d)} temos: {(moeda.diminuir(d, True))}')
    sleep(2)
    ask=str(input('Quer continuar? [S/N] ')).upper() .strip()
    if ask in 'N':
        break
print('Encerrando programa...')
