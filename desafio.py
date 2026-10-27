
import os

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
mensagem = ""

while True:

    # Limpa a tela antes de redesenhar o menu
    os.system("cls" if os.name == "nt" else "clear")

    menu = f"""
+==========================================+
|              BANCO PYTHON                |
+==========================================+
|                                          |
|  SALDO DISPONIVEL                        |
|  R$ {saldo:>12.2f}                       |
|                                          |
|  Saques disponiveis: {LIMITE_SAQUES - numero_saques} de {LIMITE_SAQUES}                 |
+==========================================+
|              MENU PRINCIPAL              |
+==========================================+
|                                          |
|  [D] Depositar                           |
|  [S] Sacar                               |
|  [E] Consultar extrato                   |
|  [Q] Sair                                |
|                                          |
+==========================================+
"""

    print(menu)

    if mensagem:
        print(mensagem)
        print("-" * 44)

    mensagem = ""
    opcao = input("=> Selecione uma operacao: ").lower().strip()

    if opcao == "d":
        try:
            valor = float(input("\nValor do deposito: R$ "))

            if valor > 0:
                saldo += valor
                extrato += f"Deposito: R$ {valor:.2f}\n"
                mensagem = f"Deposito de R$ {valor:.2f} realizado com sucesso!"
            else:
                mensagem = "Operacao falhou! Valor invalido."

        except ValueError:
            mensagem = "Operacao falhou! Digite um numero valido."

    elif opcao == "s":
        try:
            valor = float(input("\nValor do saque: R$ "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                mensagem = "Operacao falhou! Saldo insuficiente."

            elif excedeu_limite:
                mensagem = "Operacao falhou! Limite de R$ 500.00 excedido."

            elif excedeu_saques:
                mensagem = "Operacao falhou! Limite de saques atingido."

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                mensagem = f"Saque de R$ {valor:.2f} realizado com sucesso!"

            else:
                mensagem = "Operacao falhou! Valor invalido."

        except ValueError:
            mensagem = "Operacao falhou! Digite um numero valido."

    elif opcao == "e":
        os.system("cls" if os.name == "nt" else "clear")

        print("+==========================================+")
        print("|             EXTRATO BANCARIO             |")
        print("+==========================================+")
        print()
        print("Nao foram realizadas movimentacoes."
              if not extrato else extrato)
        print("-" * 44)
        print(f"SALDO ATUAL: R$ {saldo:.2f}")
        print("=" * 44)

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "q":
        os.system("cls" if os.name == "nt" else "clear")
        print("Obrigado por utilizar o Banco Python!")
        break

    else:
        mensagem = "Operacao invalida! Selecione uma opcao do menu."
