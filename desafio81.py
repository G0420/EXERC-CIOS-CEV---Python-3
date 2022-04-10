lista=[]
while True:
    numeros=int(input('Digite um valor: [0 PARA PARAR!] '))
    if numeros==0:
        break
    else:
        lista.append(numeros)
print(f'Você digitou {len(lista)} números!')
print(f'A ordem DECRESCENTE deles é {lista.sort(reverse=True)}')

if 5 in lista:
    print('O número 5 faz parte da lista!')
else:
    print('Você não digitou o número 5!')