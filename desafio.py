from datetime import datetime

data = datetime.now()

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}. Data/Hora: {datetime.now()}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido do dia.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}. Data/Hora: {datetime.now()}\n"
        saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")

    filtragem = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    # Verifica se a lista está vazia
    if (filtragem[0] if filtragem else None):
        print("Já existe um usuário com esse CPF.")
        return
    
    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    filtragem = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    # Verifica se a lista está vazia
    if (filtragem[0] if filtragem else None):
        print("Conta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": filtragem[0]}
    
    print("Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        print(f"Agencia: {conta['agencia']} C/C: {conta['numero_conta']} Titular: {conta['usuario']['nome']}")

def menu():
    menu = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(menu)

def main():
    saldo = 0
    limite = 500
    AGENCIA = "0001"
    extrato = ""
    saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, saques=saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

main()
