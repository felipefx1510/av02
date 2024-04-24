# login.py
from time import sleep
def login(usuarios_cadastrados): # entre parentes está chamando a variável global
    
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

    # verificar se o nome de usuario e senha são válidos
    if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha:
        print(f'Login bem-sucedido! Bem-vindo, {usuario}!')
        if usuario == 'adm':
            opcao = int(input('Você é o administrador. Deseja criar um novo usuário?\n1. Sim\n2. Não\n'))
            if opcao == 1:
                novo_usuario = input('Digite o nome do novo usuário: ')
                nova_senha = input('Digite a senha do novo usuário: ')
                #usuario adicionado
                usuarios_cadastrados[novo_usuario] = nova_senha
                print('Novo usuário criado com sucesso!')
                opcao_usuario = int(input('Deseja adicionar mais um usuário?\n1. Sim\n2. Não\n'))
                while opcao_usuario == 1:
                    novo_usuario = input('Digite o nome do novo usuário: ')
                    nova_senha = input('Digite a senha do novo usuário: ')
                    usuarios_cadastrados[novo_usuario] = nova_senha
                    print('Novo usuário criado com sucesso!')
                    opcao_usuario = int(input('Deseja adicionar mais um usuário?\n1. Sim\n2. Não\n'))
                    break
                print('Faça seu login novamente para continuar.')
                login(usuarios_cadastrados)  # Reautenticação após o administrador decidir não adicionar mais usuários
            if opcao == 2:
                print('Você escolheu não adicionar um novo usuário.')
                print('Indo para o menu...')
                sleep(2)

        else:
            print('Você não é o administrador.')
            print('Indo para o menu...')
            sleep(2)
    else:
        print('Nome de usuário ou senha incorretos. Por favor, tente novamente.')
        login(usuarios_cadastrados)