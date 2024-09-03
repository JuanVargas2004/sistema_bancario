import os
import keyboard

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def printcenter(x):
    print(x.center(75))

def main():

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


        print(paybank) #75


        printcenter("Bem Vindo ao PayBank!! O que deseja fazer por agora?\n")

        opcoes = '''
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

        if tecla:
            break


main()