from time import sleep
def linha():
    print('=-'*15)

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(1)
    if i<f:
        cont=i
        while cont<=f:
            print(f'{cont} ',end='')
            sleep(0.3)
            cont+=p
        print('FIM!')
    else:
        cont=i
        while cont>=f:
            print(f'{cont} ',end='')
            sleep(0.3)
            cont-=p
        print('FIM!')
contador(1,10,1)
contador(10,0,2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
inicio=int(input('Início: '))
fim=int(input('Fim: '))
passo=int(input('Passo: '))
contador(inicio, fim, passo)
