numeros=[]
soma=0
#loop dos números da lista!
while True:
    n=int(input('Digite um valor: '))
    soma+=n
    if n not in numeros:
        numeros.append(n)
        print('Valor inserido com sucesso!')
    else:
        print('Opa, esse valor já foi digitado antes, não vai entrar na lista!')

    r=str(input('Quer continuar? [S/N] '.upper().strip()))
    print('='*10)
    if r=='N':
        break

numeros.sort()
print('-='*30)
print(f'Você digitou {len(numeros)} números, são eles: {numeros}')
print(f'O MENOR número dessa sequência é o {min(numeros)}')
print(f'O MAIOR número dessa sequência é o {max(numeros)}')
print(f'O resultado da  soma entre eles é {soma}')
print(f'a ordem sequencial deles é {numeros}')
print('=-'*30)
