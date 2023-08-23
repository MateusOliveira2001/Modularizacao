class Lista():

    def __init__(self):
        self.atividades = []

    def adicionar(self, atividade):
        if atividade not in self.atividades:
            print('Atividade não encontrada')
        self.atividades.append(atividade)
    
    def excluir(self, atividade):
        if atividade not in self.atividades:
            print('Atividade não encontrada')
        self.atividades.remove(atividade)
    
    def editar(self, atividade):
        if atividade not in self.atividades:
            print('Atividade não encontrada')
        nova_atividade = input('Descreva a correção: ')
        idx = self.atividades.index(atividade)
        self.atividades.insert(idx, nova_atividade)
        self.atividades.remove(atividade)

    def mostra_lista(self):
        print('+' + '-'*47 + '+')
        print('|', end='')
        print('\t\tLista de atividades\t\t',end='' )
        print('|')
        print('+' + '-'*47 + '+')
        i=0
        for atividade in self.atividades:
            print('|', end='')
            print('{0:30}  {1:15}'.format(atividade,i), end='')
            print('|')
            i+=1

        print('+' + '-'*47 + '+')
