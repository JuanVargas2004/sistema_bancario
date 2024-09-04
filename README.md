# PayBank - Sistema de Gerenciamento Bancário

Bem-vindo ao PayBank! Este é um sistema de gerenciamento bancário simples implementado em Python. O PayBank permite realizar depósitos, saques e visualizar extratos de transações.

## Funcionalidades

- **Depositar**: Adicione um valor ao saldo da conta.
- **Sacar**: Retire um valor da conta, com um limite de 3 saques por dia.
- **Ver Extrato**: Visualize todas as transações realizadas.
- **Sair**: Encerre o programa.

## Requisitos

- Python 3.x
- Biblioteca `keyboard` (pode ser instalada via `pip install keyboard`)

## Como Usar

1. **Executar o Programa**: Para iniciar o PayBank, execute o script Python fornecido.

   ```bash
   python paybank.py

2. **Interação com o Menu:**

- ***Depositar:*** Pressione `1` e informe o valor do depósito.

- ***Sacar:*** Pressione `2` e informe o valor do saque (máximo de 3 saques por dia).

- ***Ver Extrato:*** Pressione `3` para visualizar o histórico de transações. Pressione Q para sair da tela de extratos.

- ***Sair:*** Pressione `0` para sair do PayBank

## Código

O script consiste em um menu interativo que permite ao usuário realizar as operações acima. O código é estruturado da seguinte forma:

- **Função `limpar()`**: Limpa o terminal para uma visualização mais clara.
- **Função `printcenter(x)`**: Imprime uma string centralizada no terminal.
- **Função `sair()`**: Gerencia a saída da tela de extratos ao pressionar `Q`.
- **Função `main()`**: Gerencia o fluxo principal do programa, exibindo o menu e processando as escolhas do usuário.