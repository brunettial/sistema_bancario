menu = """
==================== Menu =====================

-Escolha uma opção:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

================================================
"""

saldo = 1470.00 
deposito = ""
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
       
        valor = float(input("Qual valor você gostaria de depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Erro na operação! O valor informado é invalido!")

    elif opcao == "2":
        print("Saque")

        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação inválida! O valor de saque excedeu o limite.")
        
        elif excedeu_saques:
            print("Operação inválida! Limite máximo de saque excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Erro na operação! O valor informado é invalido.")


    elif opcao == "3":
        print("\n============ Extrato =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")

    elif opcao == "4":
        print("Agradecemos a preferencia, tenha um bom dia!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
    