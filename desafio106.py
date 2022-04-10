def ajuda(msg):
  help(msg)

def titulo(msg,cor=0):
    tam=len(msg)+4
    print('='*tam)
    print(f'  {msg}')
    print('='*tam)
n=''
while True:
    titulo('SISTEMA DE AYUDA PyHELP')
    n=str(input('Digite uma função padrão do Python: '))
    if n.upper() == 'FIM':
        break
    else:
        ajuda(n)
titulo('Encerrando programa...')
