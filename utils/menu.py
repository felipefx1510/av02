from time import sleep

def voltando_menu():
    print('Voltando para o menu...')
    sleep(2)
    
def menu(lanches):
    print('-'*30)
    print('Menu:')
    print('1 - Cadastrar novo lanche')
    print('2 - Listar lanches')
    print('3 - Buscar lanche por nome')
    print('4 - Remover lanche')
    print('5 - Atualizar lanche')
    print('0 - Sair')
    opcao = int(input('Escolha uma opção: '))
    
    if opcao == 1:
        while True:
            nome = str(input('Digite o nome do produto: ')).lower()
            valor = float(input('Digite o valor do produto: '))
            lanches[nome] = valor
            print('Produto cadastrado com sucesso!')
            opcao = int(input('Deseja adicionar outro produto?\n1. Sim\n2. Não\n'))
            if opcao != 1:
                break
        voltando_menu()
        return menu(lanches)
    
    elif opcao == 2:
        print('Lista de lanches:')
        for nome, valor in lanches.items():
            print(f'{nome}: R${valor:.2f}')
        voltando_menu()
        return menu(lanches)
    
    elif opcao == 3:
        while True:
            nome = input('Digite o nome do produto que deseja buscar: ').lower()
            if nome in lanches:
                print(f'{nome}: R${lanches[nome]:.2f}')
            else:
                print('Produto não encontrado. Tente novamente')
            opcao = int(input('Deseja buscar outro produto?\n1. Sim\n2. Não\n'))
            if opcao != 1:
                break
        voltando_menu()
        return menu(lanches)
    
    elif opcao == 4:
        while True:
            nome = input('Digite o nome do produto que deseja remover: ').lower()
            if nome in lanches:
                del lanches[nome]
                print('Produto removido com sucesso!')
            else:
                print('Produto não encontrado. Tente novamente')
            opcao = int(input('Deseja excluir outro produto?\n1. Sim\n2. Não\n'))
            if opcao != 1:
                break
        voltando_menu()
        return menu(lanches)
    
    elif opcao == 5:
        while True:
            nome = input('Digite o nome do produto que deseja atualizar: ').lower()
            if nome in lanches:
                valor = float(input('Digite o novo valor do produto: '))
                lanches[nome] = valor
                print('Produto atualizado com sucesso!')
            else:
                print('Produto não encontrado. Tente novamente')
            opcao = int(input('Deseja atualizar outro produto?\n1. Sim\n2. Não\n'))
            if opcao != 1:
                break
        voltando_menu()
        return menu(lanches)
    
    elif opcao == 0:
        print('Saindo...')
        sleep(2)
        return
    
    else:
        print('Opção inválida, tente novamente!')
        voltando_menu()
        menu(lanches)
