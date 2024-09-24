menu = """
============================= SISTEMA BANCÁRIO =============================

Bem-vindo ao Sistema Bancário em Python, Selecione uma opção para continuar!
Utilize os números do teclado! 

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

======== desenvolvido por: William Ramos / realease: 13/09/2024 =============
=> """

titulo_extrato = " EXTRATO BANCÁRIO "
valor = 0.0
saldo = 0
limite_saque = 500
limite_saque_dia = 3
numero_saques = 0
extrato = ""

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0.0:
            #saldo = saldo + valor #apenas por ser didático
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação concluída!")
        else:
            print("Operação falhou! Valor digitado inválido.")
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saque = numero_saques > limite_saque_dia

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
            print(f"Seu Saldo Atual = R$ {saldo:.2f}")
        elif excedeu_limite:
            print("Operação falhou! Valor digitado acima do limite estabelecido.")
            print(f"Seu Limite/saque = R$ {limite_saque:.2f}")
        elif excedeu_saque:
            print("Operação falhou! Valor digitado acima do limite estabelecido.")
            print(f"Seu Limite de Saque por dia = {limite_saque_dia} saques.")
        elif valor > 0.0:
            #saldo = saldo - valor #apenas por ser didático
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação concluída!")
        
        else:
            print("Operação falhou! Valor digitado é inválido.")
    elif opcao == "3":
        print(titulo_extrato.center(50,"#"))
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("".center(50,"#"))
    
    elif opcao == "4":
        print("Obrigado por utilizar nosso Sistema Bancário!!")
        break
    
    else:
        print("Operação inválida, digite outra opção desejada.")