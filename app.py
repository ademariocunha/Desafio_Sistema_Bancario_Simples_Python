import datetime

saldo = 0.0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def menu():
    print("""
========== BANCO PY ==========
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
""")

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\nHorario: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}"
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("⚠️ Valor inválido para depósito.")

def sacar(valor):
    global saldo, extrato, numero_saques
    if numero_saques >= LIMITE_SAQUES:
        print("⚠️ Limite diário de saques atingido.")
    elif valor > saldo:
        print("⚠️ Saldo insuficiente.")
    elif valor > limite_saque:
        print(f"⚠️ Limite máximo por saque é R$ {limite_saque:.2f}.")
    elif valor <= 0:
        print("⚠️ Valor de saque deve ser positivo.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\nHorario: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}"
        numero_saques += 1
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")

def mostrar_extrato():
    print("\n========== EXTRATO ==========")
    print(extrato if extrato else "Nenhuma movimentação registrada.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==============================\n")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        depositar(valor)
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))
        sacar(valor)
    elif opcao == "3":
        mostrar_extrato()
    elif opcao == "0":
        print("✅ Obrigado por usar o Banco PY!")
        break
    else:
        print("❌ Opção inválida. Tente novamente.")
