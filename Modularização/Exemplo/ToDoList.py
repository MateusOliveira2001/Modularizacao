from Pacote import Lista

lista = Lista()

while True:
    print('O que deseja realizar agora?')
    print('')
    print('Adicionar tarefa -> Digite "A"')
    print('')
    print('Excluir tarefa -> Digite "X"')
    print('')
    print('Editar tarefa -> Digite "E"')
    print('')
    print('Encerrar -> Digite: "Sair"')
    print('')
    operação = input('Operação selecionada: ')

    if operação == 'A':
        atividade = input('Descreva a atividade: ')
        lista.adicionar(atividade)

    if operação == 'X':
        atividade = input('Digite a atividade que deseja excluir: ')
        lista.excluir(atividade)

    if operação == 'E':
        atividade = input('Digite a atividade que deseja editar: ')
        lista.editar(atividade)
    
    if operação == 'Sair':
        break
    
    print("\n" * 130)
    lista.mostra_lista()
    print()
