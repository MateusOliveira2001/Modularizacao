atividades = []

def adicionar(atividade):
    if atividade in atividades:
        print('Atividade já cadastrada na lista')
    atividades.append(atividade)


def excluir(atividade):
    if atividade not in atividades:
        print('Atividade não encontrada')
    atividades.remove(atividade)


def editar(atividade):
    if atividade not in atividades:
        print('Atividade não encontrada')
    nova_atividade = input('Descreva a correção: ')
    idx = atividades.index(atividade)
    atividades.insert(idx, nova_atividade)
    atividades.remove(atividade)


def mostra_lista(atividades):
    print('+' + '-'*47 + '+')
    print('|', end='')
    print('\t\tLista de atividades\t\t',end='' )
    print('|')
    print('+' + '-'*47 + '+')
    i=0
    for atividade in atividades:
        print('|', end='')
        print('{0:30}  {1:15}'.format(atividade,i), end='')
        print('|')
        i+=1

    print('+' + '-'*47 + '+')