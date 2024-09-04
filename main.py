import os
import time
import keyboard

movimentacoes = []
saldo = 0

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def printcenter(x):
    print(x.center(83))

def main():
    global saldo
    global movimentacoes

    while True:

        limpar()

        paybank = '''
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        *       ____                             ____                     __      *
        *      / __ \  ____ _   __  __          / __ )  ____ _   ____    / /__    *
        *     / /_/ / / __ `/  / / / /         / __  | / __ `/  / __ \  / //_/    *
        *    / ____/ / /_/ /  / /_/ /         / /_/ / / /_/ /  / / / / / ,<       *
        *   /_/      \__,_/   \__, /         /_____/  \__,_/  /_/ /_/ /_/|_|      *
        *                    /____/                                               *
        *                                                                         *
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        '''


        print(paybank) #83


        printcenter("Bem Vindo ao PayBank!! O que deseja fazer por agora?\n")

        opcoes = '''\n
        Escolha uma das opções abaixo...
        — — — — — — — — — — — — — — —
        |   [1] - Depositar         |
        |   [2] - Sacar             |
        |   [3] -  Ver Extrato      |
        |   [0] - Sair do PayBank   |
        — — — — — — — — — — — — — — —
        '''

        centralizado = "\n".join(line.center(75) for line in opcoes.splitlines())

        print(centralizado)

        tecla = keyboard.read_event(suppress=True).name

        if tecla == "1":
            printcenter("Opção \"Depositar\" foi escolhida\n\n")
            deposito = float(input("Quanto deseja depositar? R$"))
            if deposito > 0:
                movimentacoes.append(f"Deposito: R$ {deposito:.2f}")
                saldo += deposito
            else:
                printcenter("Valor inválido. Tente novamente.")
                time.sleep(.8)
                continue    
            break

        elif tecla == "2":
            printcenter("Opção \"Sacar\" foi escolhida\n\n")

            saque = float(input("Quanto deseja sacar? R$"))

            if saque > 0 and saque <= saldo:
                movimentacoes.append(f"Saque: R$ {saque:.2f}")
                saldo -= saque
                printcenter(f"Saque realizado com sucesso!\nSeu novo saldo é: R$ {saldo:.2f}")

            else:
                print("Valor inválido. Tente novamente.")
                time.sleep(.8)
            break

        elif tecla == "3":
            printcenter("Opção \"Ver Extrato\" foi escolhida\n\n")
            break

        elif tecla == "0":
            printcenter("Saindo do PayBank...")
            break

        else:
            printcenter("Opção inválida. Tente novamente.")
            time.sleep(.8)

main()