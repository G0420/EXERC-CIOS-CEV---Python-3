lista=[[], []]
for l in range(0,7):
    numero=int(input(f'Digite o {l+1}° valor: '))
    if numero %2==0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print(f'os números {lista[0]} são PARES!')
print(f'e os números {lista[1]} são ÍMPARES!')
