import os

def exibir_titulo():
    print("""
███████████████████████████████████████████████████████████████████████████████████
██▀▄─██─▄─▄─█▄─▄█▄─█─▄█▄─▄█▄─▄▄▀██▀▄─██▄─▄▄▀█▄─▄▄─███─▄▄─█▄▄▄░███▄─▄▄─███─▄▄─█░█░██
██─▀─████─████─███▄▀▄███─███─██─██─▀─███─██─██─▄█▀███─██─██▄▄░████─▄█▀███─██─█▄▄░██
▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▄▀▀▀▄▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▀▄▄▄▄▀▀▀▄▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀
""")

#----------

def pares():
    soma_pares = 0
    for i in range(1, 11, 1):
        soma_pares += i
    print(soma_pares)
    voltar_ao_menu_principal()

def impares():
    soma_impares = 0
    for i in range(1, 11, 2):
        soma_impares += i
    print(soma_impares)
    voltar_ao_menu_principal()

#----------

def crescente():
    for i in range(0, 11, +1):
        print(i)
    voltar_ao_menu_principal()    
     
def decrescente():
    for i in range(10, 0, -1):
        print(i)
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
    print('1. Somar pares')
    print('2. Somar impares')
    print('3. Crescente')
    print('4. Decrescente')
    print('5. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções: '))

        if opcao_escolhida == 1:
            pares()
        elif opcao_escolhida == 2:
            impares()
        elif opcao_escolhida == 3:
            crescente()
        elif opcao_escolhida == 4:
            decrescente()
        elif opcao_escolhida == 5:
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