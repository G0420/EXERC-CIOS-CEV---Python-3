matriz=[[0,0,0],[0,0,0],[0,0,0]]
somapar=somatres=maiorlinha=0
for c in range(0,3):
    for n in range(0,3):
        matriz[c][n]=int(input(f'Digite um valor para a matriz [{c},{n}] '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end='')
        if matriz[l][c] %2==0:
            somapar+=matriz[l][c]
    print()
for l in range(0,3):
    somatres+=matriz[l][2]
print(f'A soma de todos os valores pares digitados é {somapar}')
print(f'A soma dos valores da terceira coluna é {somatres}')
print(f'E o maior valor da segunda linha foi o {max(matriz[1])}')