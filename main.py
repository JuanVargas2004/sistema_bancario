import os
import sys
import time
import keyboard

movimentacoes = []
saldo = 0
count_saques = 0

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def printcenter(x):
    print(x.center(83))

def sair():
    tecla3 = keyboard.read_event(suppress=True).name

    if tecla3 == "Q" or tecla3 == "q":
        print("Saindo do tela de extratos...")
        time.sleep(1)
    else:
        sair()

def main():
    global saldo
    global movimentacoes
    global count_saques

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
        |   [3] - Ver Extrato       |
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
                printcenter(f"Depósito de R${deposito:.2f} realizado com sucesso!")
                movimentacoes.append(f"Depósito: R$ {deposito:.2f}")
                saldo += deposito
                time.sleep(2)
                continue
            else:
                printcenter("Valor inválido. Tente novamente.")
                time.sleep(.8)
                continue    


        elif tecla == "2":
            printcenter("Opção \"Sacar\" foi escolhida\n\n")

            saque = float(input("Quanto deseja sacar? R$"))
            if count_saques < 3:
                if saque > 0 and saque <= saldo:
                    movimentacoes.append(f"Saque: R$ {saque:.2f}")
                    saldo -= saque
                    count_saques += 1
                    printcenter(f"Saque realizado com sucesso!")
                    printcenter(f"Seu saldo agpra é: R$ {saldo:.2f}")
                    time.sleep(2)
                    continue

                else:
                    print("Valor inválido. Tente novamente.")
                    time.sleep(.8)
                    continue
            else:
                printcenter("Você atingiu o limite de 3 saques no dia.")
                time.sleep(.8)
                continue

        elif tecla == "3":
            printcenter("Opção \"Ver Extrato\" foi escolhida\n\n")
            
            print(("#" * 25).center(83))
            for movimento in movimentacoes:
                printcenter(movimento)
            print(("#" * 25).center(83))
            
            time.sleep(1.5)
            print("\n\nPressione a letra \"Q\" para sair da tela de extratos")
            
            sair()

        elif tecla == "0":
            printcenter("Saindo do PayBank...")
            break

        else:
            printcenter("Opção inválida. Tente novamente.")
            time.sleep(.8)

main()