def linha():
    print('=-'*15)
def maior(*valores):
    print(f'Foram informados {len(valores)} valores.')
    print(f'dentre eles, o {max(valores)} é o maior!')
    linha()
maior(4,5,6,7,3)
maior(2,4)
maior(5,6,7)