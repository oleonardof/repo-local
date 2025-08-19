from datetime import datetime
from zoneinfo import ZoneInfo  # disponível no Python 3.9+

# =========================
# Configurações do Sistema
# =========================
LIMITE_SAQUES = 3
LIMITE_VALOR = 500
SENHA = "1234"  # senha fixa de exemplo

# Definindo fuso horário de Brasília
FUSO = ZoneInfo("America/Sao_Paulo")

def agora():
    """Retorna a data/hora atual no fuso de Brasília"""
    return datetime.now(FUSO)

# =========================
# Funções do Sistema
# =========================
def autenticar():
    tentativas = 3
    while tentativas > 0:
        senha = input("Digite sua senha de 4 dígitos: ")
        if senha == SENHA:
            print("✅ Acesso liberado!\n")
            return True
        else:
            tentativas -= 1
            print(f"❌ Senha incorreta. Tentativas restantes: {tentativas}")
    print("🚫 Acesso bloqueado.")
    return False

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"{agora().strftime('%d/%m %H:%M')} - Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")
    return saldo, extrato

def sacar(valor, saldo, extrato, numero_saques):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > LIMITE_VALOR:
        print("O saque excede o limite de R$ 500,00.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"{agora().strftime('%d/%m %H:%M')} - Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Valor inválido.")
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n=========== EXTRATO ===========")
    print("Sem movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===============================")

# =========================
# Programa Principal
# =========================
if autenticar():  # só entra no sistema se passar pela senha
    saldo = 0
    extrato = ""
    numero_saques = 0

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(valor, saldo, extrato)
            except ValueError:
                print("Entrada inválida. Digite um número.")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques)
            except ValueError:
                print("Entrada inválida. Digite um número.")

        elif opcao == "e":
            mostrar_extrato(saldo, extrato)

        elif opcao == "q":
            print("Sessão encerrada. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
