numeros=[]
maior=menor=0
for n in range(0,5):
    numeros.append(int(input('Digite um valor: ')))
print(f'O MENOR número digitado foi {min(numeros)} e está na posição {numeros.index(min(numeros))}',end='')
print()
print(f'O MAIOR número digitado foi {max(numeros)} e está na posição {numeros.index(max(numeros))}',end='')

