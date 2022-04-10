def linha():
    print('    CONTROLE DE TERRENOS')
    print('='*30)
linha()
def area(larg, comp):
    a=larg*comp
    print(f'A área de um terreno de {larg}X{comp} é de {a:.2f}m².')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)