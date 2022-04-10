numeros=[]
for n in range(0,5):
    num=int(input('Digite um valor: '))
    if n==0 or num>numeros[-1]:
        numeros.append(num)
        print('Número adicionado ao FINAL da lista!')
    else:
        pos=0
        while pos<len(numeros):
            if num<=numeros[pos]:
                numeros.insert(pos, num)
                print('Número adicionado ao COMEÇO da lista')
                break
            pos+=1

print(f'os números digitados em ordem foram: {numeros}')
