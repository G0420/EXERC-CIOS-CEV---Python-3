def linha():
    print('='*30)

def notas(*n, sit=False):
    """
    =Função feita na aula do professor Gustavo Guanabara do canal "Curso em vídeo" no YouTube, proposta para analisar notas de vários alunos e dar as informações sobre elas.
    :param n: notas dos alunos
    :param sit: digite "sit=True" para mostrar a situação de acordo com a média do aluno, "sit=False" para ignorar a função.
    :return:
    """
    geral = {}
    geral['tam']=len(n)
    geral['min']=min(n)
    geral['max']=max(n)
    geral['media']=sum(n)/len(n)
    print(f'Ao todo você informou {geral["tam"]} nota(s), a MAIOR foi {geral["max"]}, a MENOR foi {geral["min"]}, a MÉDIA entre elas é {geral["media"]}')
    if sit==True:
        if geral['media']<7:
            print('A situação tá feia!',end='')
        else:
            print('Boa, tá acima da média!',end='')

notas(10,9,8, sit=True)
help(notas)