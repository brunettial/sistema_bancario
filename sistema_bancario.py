menu = """\033[33m
==================== Menu =====================

-Escolha uma opção:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

================================================\033[m
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
            print("\033[31mErro na operação! O valor informado é invalido!\033[33m")

    elif opcao == "2":
        print("Saque")

        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\033[31mOperação inválida! Você não possui saldo suficiente.\033[m")

        elif excedeu_limite:
            print("\033[31mOperação inválida! O valor de saque excedeu o limite.\033[m")
        
        elif excedeu_saques:
            print("\033[31mOperação inválida! Limite máximo de saque excedido.\033[m")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("\033[31mErro na operação! O valor informado é invalido.\033[m")


    elif opcao == "3":
        print("\n============ Extrato =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")

    elif opcao == "4":
        print("\033[32mAgradecemos a preferencia, tenha um bom dia!\033[m")
        break

    else:
        print("\033[31mOperação inválida, por favor selecione novamente a operação desejada\033[m")
    