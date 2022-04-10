from random import randint
lista=[]
def linha():
    print('=-'*15)
def sorteia(lista):
    for n in range(0,5):
        lista.append(randint(0,10))
    print(f'Sorteando 5 valores pra lista: {lista} ')
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
sorteia(lista)
somapar(lista)
#100 EXERCÍCIOS CONCLUÍDOS, PQP!!!