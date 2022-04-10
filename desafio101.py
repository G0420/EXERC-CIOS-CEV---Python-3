def linha():
    print('='*30)
ano=2022
def voto(n=0):
    if n<16:
        return 'nvota'
    if n>=18 and n<65:
        return 'vota'
    elif n>64:
        return 'se'
votação = int(input('Digite o ano em que você nasceu: '))
age=ano-votação
if voto(age)=='nvota':
    print(f'Com {age} anos de idade, NÃO VOTA!')
if voto(age)=='vota':
    print(f'Com {age} anos de idade, VOTO OBRIGATÓRIO!')
if voto(age)=='se':
    print(f'Com {age} anos de idade, VOTO OPCIONAL!')
