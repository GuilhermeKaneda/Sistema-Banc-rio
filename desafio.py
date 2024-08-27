from datetime import datetime, timedelta

saldo = 0
limite = 500
extrato = ""
saques = 0
LIMITE = 3
data = datetime.now()

while True:
    opcao = input("[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n=> ")

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif saques >= LIMITE:
            print("Operação falhou! Número máximo de saques excedido do dia.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}. Data/Hora: {datetime.now()}\n"
            if datetime.now() - data >= timedelta(days=1):
                data = datetime.now()
                saques = 0
            else:
                saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")