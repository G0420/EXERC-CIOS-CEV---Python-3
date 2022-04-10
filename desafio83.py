expr=(str(input('Digite uma expressão: ')))
numero=[]
for s in expr:
    if s=='(':
        numero.append('(')
    elif s==')':
        if len(numero)>0:
            numero.pop()
        else:
            numero.append(')')
            break
if len(numero)==0:
    print(f'A expressão {expr} é VÁLIDA!')
else:
    print(f'A expressão {expr} é INVÁLIDA')
