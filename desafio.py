def exibir_menu():
    return """  
[1] Depositar  
[2] Sacar  
[3] Extrato  
[0] Sair  

=> """  

def depositar(saldo, extrato):
    valor = float(input("Informe o valor a ser depositado: "))  
    if valor > 0:  
        saldo += valor  
        extrato += f"Depósito: R$ {valor:.2f}\n"  
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")  
    else:  
        print("Valor inválido para depósito.")  
    return saldo, extrato  

def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    valor = float(input("Informe o valor a ser sacado: "))  
    if numero_saques < LIMITE_SAQUES and valor <= saldo and valor <= limite:  
        saldo -= valor  
        extrato += f"Saque: R$ {valor:.2f}\n"  
        numero_saques += 1  
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")  
    else:  
        print("Saque não realizado. Verifique o saldo, limite ou número de saques.")  
    return saldo, extrato, numero_saques  

def exibir_extrato(saldo, extrato):
    print("=== EXTRATO ===")  
    print(extrato if extrato else "Não foram realizadas movimentações.")  
    print(f"Saldo atual: R$ {saldo:.2f}")  

saldo = 4000  
limite = 500  
extrato = ""  
numero_saques = 0  
LIMITE_SAQUES = 3  

while True:  
    opcao = input(exibir_menu())  

    if opcao == "1":  
        saldo, extrato = depositar(saldo, extrato)  
    elif opcao == "2":  
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)  
    elif opcao == "3":  
        exibir_extrato(saldo, extrato)  
    elif opcao == "0":  
        print("Encerrando o programa...")  
        break  
    else:  
        print("Operação inválida, por favor selecione novamente a operação desejada.")  