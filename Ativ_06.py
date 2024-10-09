import os

lista_de_numeros = []
lista_valores = []

def exibir_titulo():
    print("""

░█████╗░████████╗██╗██╗░░░██╗██╗██████╗░░█████╗░██████╗░███████╗  ███████╗  ███████╗  ░█████╗░
██╔══██╗╚══██╔══╝██║██║░░░██║██║██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔════╝  ██╔════╝  ██╔═══╝░
███████║░░░██║░░░██║╚██╗░██╔╝██║██║░░██║███████║██║░░██║█████╗░░  ██████╗░  █████╗░░  ██████╗░
██╔══██║░░░██║░░░██║░╚████╔╝░██║██║░░██║██╔══██║██║░░██║██╔══╝░░  ╚════██╗  ██╔══╝░░  ██╔══██╗
██║░░██║░░░██║░░░██║░░╚██╔╝░░██║██████╔╝██║░░██║██████╔╝███████╗  ██████╔╝  ███████╗  ╚█████╔╝
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░  ╚══════╝  ░╚════╝░
""")

#----------

def soma():
    print("\nDigite o numero que deseja acrescentar a lista de soma.")
    new_numb = int(input(''))
    lista_de_numeros.append(new_numb)
    print(f'\nO nome {new_numb} foi cadastrado com sucesso!')
    soma_na_lista()

def lista_soma():
    print('Lista de números:')
    for list_number in lista_de_numeros:
        print(f'.{list_number}')
    soma_na_lista()

def soma_na_lista():
    print('\nEscolha uma das opções abaixo')
    print('1. Adicionar outro número')
    print('2. Exibir lista de números')
    print('3. Calcular')
    print('4. Voltar ao menu principal')
    print('5. Sair')
    
    try:
        opcao_escolhida = int(input('\nEscolha uma das opções: '))

        if opcao_escolhida == 1:
            soma()
        elif opcao_escolhida == 2:
            lista_soma()
        elif opcao_escolhida == 3:
            soma_calc()
        elif opcao_escolhida == 4:
            voltar_ao_menu_principal()
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()    

def soma_calc():
    soma = 0

    try:
        for numero in lista_de_numeros:
            soma += numero
        print(f"Soma dos elementos: {soma}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    voltar_ao_menu_principal()

def media():
    print("\nDigite o numero que deseja acrescentar a lista de média.")
    new_med = int(input(''))
    lista_valores.append(new_med)
    print(f'\nO nome {new_med} foi cadastrado com sucesso!')
    media_na_lista()

def lista_media():
    print('Lista de números:')
    for list_numb_media in lista_valores:
        print(f'.{list_numb_media}')
    media_na_lista()

def media_na_lista():
    print('\nEscolha uma das opções abaixo')
    print('1. Adicionar outro número')
    print('2. Exibir lista de números')
    print('3. Calcular média')
    print('4. Voltar ao menu principal')
    print('5. Sair')
    
    try:
        opcao_escolhida = int(input('\nEscolha uma das opções: '))

        if opcao_escolhida == 1:
            media()
        elif opcao_escolhida == 2:
            lista_soma()
        elif opcao_escolhida == 3:
            media_calc()
        elif opcao_escolhida == 4:
            voltar_ao_menu_principal()
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()  

def media_calc():
    soma_valores = 0

    try:
        for valor in lista_valores:
            soma_valores += valor
        media = soma_valores / len(lista_valores)
        print(f"\nMédia dos valores: {media}")
    except ZeroDivisionError:
        print("\nA lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
    media_na_lista()

#----------

def exibir_opcoes():
    print('1. Soma de lista')
    print('2. Média de lista')
    print('3. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções: '))

        if opcao_escolhida == 1:
            soma()
        elif opcao_escolhida == 2:
            media()
        elif opcao_escolhida == 3:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

#----------
def finalizar_app():
    os.system('cls')
    print('\nFinalizando o app')

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite Enter para reiniciar.')
    main()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()