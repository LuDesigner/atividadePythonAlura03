import os
lista_loop = []

def exibir_titulo():
    print("""
████████████████████████████████████████████████████████████████████████████████████████
█▄─▄███▄─▄█─▄▄▄▄█─▄─▄─██▀▄─████▄─▄▄▀█▄─▄▄─███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─█▄─▄▄▀██▀▄─██─▄▄▄▄█
██─██▀██─██▄▄▄▄─███─████─▀─█████─██─██─▄█▀███─███▀█─██─██─█▄█─███─▄▄▄██─▄─▄██─▀─██▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
""")

#----------

def lista_loop_add():
    print("\nDigite o que deseja acrescentar a lista.")
    new_lista = input('')
    lista_loop.append(new_lista)
    print(f'\nO nome {new_lista} foi cadastrado com sucesso!')
    lista_add()

def lista_add():
    print('\nEscolha uma das opções abaixo')
    print('1. Adicionar novo item')
    print('2. Exibir lista')
    print('3. Voltar ao menu principal')
    print('4. Sair')
    
    try:
        opcao_escolhida = int(input('\nEscolha uma das opções: '))

        if opcao_escolhida == 1:
            lista_loop_add()
        elif opcao_escolhida == 2:
            exibir_lista()
        elif opcao_escolhida == 3:
            main()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def exibir_lista():
    print('Lista completa: ')
    for list_exibir in lista_loop:
        print(f'.{list_exibir}')
    voltar_ao_menu_principal()

#----------

def finalizar_app():
    os.system('cls')
    print('\nFinalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite Enter para voltar ao menu principal.\n')
    main()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

#----------

def exibir_opcoes():
    print('1. Adicionar a lista')
    print('2. Exibir lista')
    print('3. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções: '))

        if opcao_escolhida == 1:
            lista_loop_add()
        elif opcao_escolhida == 2:
            exibir_lista()
        elif opcao_escolhida == 3:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()