import os

# ---------- Constantes ----------
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.0
AGENCIA = "0001"


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# ---------- Operações bancárias ----------

def deposito(saldo, valor, extrato, /):
    """Argumentos APENAS por posição (positional only)."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nOperação falhou! Valor inválido.")
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Argumentos APENAS por nome (keyword only)."""
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print(f"\nOperação falhou! Limite de R$ {limite:.2f} excedido.")
    elif excedeu_saques:
        print("\nOperação falhou! Limite de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nOperação falhou! Valor inválido.")

    return saldo, extrato, numero_saques


def extrato(saldo, /, *, extrato):
    """saldo: positional only | extrato: keyword only."""
    print("+==========================================+")
    print("|             EXTRATO BANCÁRIO             |")
    print("+==========================================+")
    print()
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("-" * 44)
    print(f"SALDO ATUAL: R$ {saldo:.2f}")
    print("=" * 44)


# ---------- Novas funções (usuário / conta) ----------

def criar_usuario(usuarios):
    """Cadastra um usuário. CPF só com números, sem duplicidade."""
    cpf = input("CPF (somente números): ").strip()

    if any(u["cpf"] == cpf for u in usuarios):
        print("\nJá existe usuário cadastrado com esse CPF.")
        return

    nome = input("Nome completo: ").strip()
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input(
        "Endereço (logradouro, nro - bairro - cidade/sigla estado): "
    ).strip()

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    })
    print("\nUsuário cadastrado com sucesso!")


def criar_conta(contas, usuarios):
    """Cria conta vinculada a um usuário existente (busca por CPF)."""
    cpf = input("CPF do titular: ").strip()

    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario is None:
        print("\nUsuário não encontrado. Cadastre o usuário primeiro.")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": AGENCIA,
        "numero": numero_conta,
        "usuario": usuario,
    })
    print(f"\nConta {numero_conta} criada com sucesso para {usuario['nome']}!")


def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return

    for conta in contas:
        print(
            f"Agência: {conta['agencia']} | "
            f"Conta: {conta['numero']} | "
            f"Titular: {conta['usuario']['nome']} "
            f"(CPF {conta['usuario']['cpf']})"
        )


# ---------- Menu principal ----------

def main():
    saldo = 0.0
    historico = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        limpar_tela()

        print(f"""
+==========================================+
|              BANCO PYTHON                |
+==========================================+
|  SALDO DISPONÍVEL                        |
|  R$ {saldo:>12.2f}                       |
|                                          |
|  Saques disponíveis: {LIMITE_SAQUES - numero_saques} de {LIMITE_SAQUES}                 |
+==========================================+
|              MENU PRINCIPAL              |
+==========================================+
|  [D] Depositar                           |
|  [S] Sacar                               |
|  [E] Consultar extrato                   |
|  [U] Novo usuário                        |
|  [C] Nova conta                          |
|  [L] Listar contas                       |
|  [Q] Sair                                |
+==========================================+
""")

        opcao = input("=> Selecione uma operação: ").lower().strip()

        if opcao == "d":
            try:
                valor = float(input("\nValor do depósito: R$ "))
                saldo, historico = deposito(saldo, valor, historico)
            except ValueError:
                print("\nOperação falhou! Digite um número válido.")
            input("\nPressione ENTER para continuar...")

        elif opcao == "s":
            try:
                valor = float(input("\nValor do saque: R$ "))
                saldo, historico, numero_saques = saque(
                    saldo=saldo,
                    valor=valor,
                    extrato=historico,
                    limite=LIMITE_VALOR_SAQUE,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )
            except ValueError:
                print("\nOperação falhou! Digite um número válido.")
            input("\nPressione ENTER para continuar...")

        elif opcao == "e":
            limpar_tela()
            extrato(saldo, extrato=historico)
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "u":
            limpar_tela()
            criar_usuario(usuarios)
            input("\nPressione ENTER para continuar...")

        elif opcao == "c":
            limpar_tela()
            criar_conta(contas, usuarios)
            input("\nPressione ENTER para continuar...")

        elif opcao == "l":
            limpar_tela()
            listar_contas(contas)
            input("\nPressione ENTER para continuar...")

        elif opcao == "q":
            limpar_tela()
            print("Obrigado por utilizar o Banco Python!")
            break

        else:
            print("\nOperação inválida! Selecione uma opção do menu.")
            input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()