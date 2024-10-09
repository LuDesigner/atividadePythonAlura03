import os

def exibir_titulo():
    print("""
          
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░░██████╗
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔════╝
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░██║░░██║╚█████╗░
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██║░░██║░╚═══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗╚█████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝░╚════╝░╚═════╝░
""")

#----------

def tabuada():
    numero_tabuada = int(input("\nDigite um número para ser multiplicado: \n"))
    for t in range(1, 11):
        resultado = numero_tabuada * t
        print(f"{numero_tabuada} x {t} = {resultado}")
    voltar_ao_menu_principal()

def divisao():
    numero_tabuada = float(input("\nDigite um número para ser dividido: \n"))
    for t in range(1, 11):
        resultado = numero_tabuada / t
        print(f"{numero_tabuada} / {t} = {resultado}")
    voltar_ao_menu_principal()

def soma():
    numero_tabuada = int(input("\nDigite um número para ser somado: \n"))
    for t in range(1, 11):
        resultado = numero_tabuada + t
        print(f"{numero_tabuada} + {t} = {resultado}")
    voltar_ao_menu_principal()

def subtracao():
    numero_tabuada = int(input("\nDigite um número para ser subtraido: \n"))
    for t in range(1, 11):
        resultado = numero_tabuada - t
        print(f"{numero_tabuada} - {t} = {resultado}")
    voltar_ao_menu_principal()

#----------

def exibir_opcoes():
    print('1. Multiplicação')
    print('2. Divisão')
    print('3. Soma')
    print('4. Subtração')
    print('5. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções: '))

        if opcao_escolhida == 1:
            tabuada()
        elif opcao_escolhida == 2:
            divisao()
        elif opcao_escolhida == 3:
            soma()
        elif opcao_escolhida == 4:
            subtracao()
        elif opcao_escolhida == 5:
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
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()