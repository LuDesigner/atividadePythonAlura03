import os
from datetime import date

nomes = []

def exibir_titulo():
    print("""
░█████╗░████████╗██╗██╗░░░██╗██╗██████╗░░█████╗░██████╗░███████╗  ░█████╗░░░███╗░░
██╔══██╗╚══██╔══╝██║██║░░░██║██║██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗░████║░░
███████║░░░██║░░░██║╚██╗░██╔╝██║██║░░██║███████║██║░░██║█████╗░░  ██║░░██║██╔██║░░
██╔══██║░░░██║░░░██║░╚████╔╝░██║██║░░██║██╔══██║██║░░██║██╔══╝░░  ██║░░██║╚═╝██║░░
██║░░██║░░░██║░░░██║░░╚██╔╝░░██║██████╔╝██║░░██║██████╔╝███████╗  ╚█████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝  ░╚════╝░╚══════╝
""")

#----------Numeros

def lista_de_numeros():
    print('1','2','3','4','5','6','7','8','9','10','',sep='\n')
    voltar_ao_menu_principal()
#----------Nomes

def  listar_de_nomes():
    print("\nDigite o nome que deseja acrescentar a lista.")
    new_nome = input('')
    nomes.append(new_nome)
    print(f'\nO nome {new_nome} foi cadastrado com sucesso!')
    nome_na_lista()

def lista_new_nomes():
    exibir_subtitulo('Lista dos nomes:')
    for list_nome in nomes:
        print(f'.{list_nome}')
    voltar_ao_menu_principal()

def nome_na_lista():
    print('\nEscolha uma das opções abaixo')
    print('1. Adicionar novo nome')
    print('2. Exibir lista de nomes')
    print('3. Voltar ao menu principal')
    print('4. Sair')
    
    try:
        opcao_escolhida = int(input('\nEscolha uma das opções: '))

        if opcao_escolhida == 1:
            listar_de_nomes()
        elif opcao_escolhida == 2:
            lista_new_nomes()
        elif opcao_escolhida == 3:
            voltar_ao_menu_principal()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

#----------Ano

def lista_ano():

    while True:
        try:
            date_user = int(input('\nQual o dia do seu nascimento, somente número! '))
            mes_user = int(input('\nQual o mês do seu nascimento, somente número! '))
            ano_user = int(input('\nQual o ano do seu nascimento, somente número! '))

            date_now = date.today()
            print(f'\nSua data de nascimento é de {ano_user}-{mes_user}-{date_user} e hoje é {date_now}')
            voltar_ao_menu_principal()
            
            if 1 <= date_user <= 31 and 1 <= mes_user <= 12 and 1950 <= ano_user <= 2024:
                break
            print('O número deve ter 2 dígitos')
        except ValueError:
            print("Você não digitou um número válido.")
            lista_ano()

#----------

def finalizar_app():
    exibir_subtitulo('\nFinalizando o app')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def voltar_ao_menu_principal():
    input('\nDigite Enter para voltar ao menu principal.\n')
    main()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

#----------

def exibir_opcoes():
    print('1. Lista de números de 1 a 10')
    print('2. Lista com nomes')
    print('3. Lista com o ano que você nasceu e o ano atual')
    print('4. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções: '))

        if opcao_escolhida == 1:
            lista_de_numeros()
        elif opcao_escolhida == 2:
            listar_de_nomes()
        elif opcao_escolhida == 3:
            lista_ano()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()