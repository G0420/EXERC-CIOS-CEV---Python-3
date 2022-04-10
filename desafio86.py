matriz=[[0,0,0],[0,0,0],[0,0,0]]
for c in range(0,3):
    for n in range(0,3):
        matriz[c][n]=int(input(f'Digite um valor para a matriz [{c},{n}] '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end='')
    print()