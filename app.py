import os

restaurantes = [{'nome': 'Subway', 'categoria': 'Fast Food', 'ativo': False}, 
                {'nome': 'McDonald\'s', 'categoria': 'Fast Food', 'ativo': True}, 
                {'nome': 'Burger King', 'categoria': 'Fast Food', 'ativo': False},
                {'nome': 'Minato', 'categoria': 'Sushi', 'ativo': False}]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_nome_do_app():    
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def voltar_ao_menu():
    input('Digite qualquer tecla para voltar ao menu principal.')
    main()

def exibir_menu():
    print('============================= Bem-vindo ao Sabor Express! =======================================\n')
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair')

def opcao_invalida():
    print('Opção inválida. ')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    limpar_tela()
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante} (ex: Fast Food, Japonês, etc): ')
    restaurantes.append({'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False})
    print(f'Restaurante "{nome_do_restaurante}" cadastrado com sucesso!\n')
    voltar_ao_menu()

def listar_restaurantes():
    limpar_tela()
    if not restaurantes:
        print('Nenhum restaurante cadastrado.\n')
    else:
        print('Restaurantes cadastrados:\n')    

        print('Nome do Restaurante'.ljust(20) + 'Categoria'.rjust(20) + 'Situação'.ljust(20))
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativo_restaurante = '  Ativo' if restaurante['ativo'] else ' Inativo'
            print(f'{nome_restaurante.ljust(20)}{categoria_restaurante.rjust(20)}{ativo_restaurante.ljust(20)}')
    voltar_ao_menu()

def ativar_restaurante():
    limpar_tela()
    nome_do_restaurante = input('Digite o nome do restaurante que deseja ativar: ')
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_do_restaurante.lower():
            restaurante['ativo'] = not restaurante['ativo']
            estado = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'Restaurante "{nome_do_restaurante}" {estado} com sucesso!\n')
            break
    else:
        print(f'Restaurante "{nome_do_restaurante}" não encontrado.\n')
    voltar_ao_menu()

def finalizar_app():
    limpar_tela()
    print('Encerrando o programa...')
    print('Obrigado por usar o Sabor Express! Até a próxima.')
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1: cadastrar_novo_restaurante()
            case 2: listar_restaurantes()
            case 3: ativar_restaurante()
            case 4: finalizar_app()
            case _: opcao_invalida()
    except:
        opcao_invalida()

def main():
    limpar_tela()
    exibir_nome_do_app()
    exibir_menu()
    escolher_opcao()
    
if __name__ == '__main__':
    main()