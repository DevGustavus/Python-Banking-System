menu = """
====== MENU ======
[1] Depositar
[2] Sacar
[3] Extrato Bancario
[4] Sair
=> """

saldo = 0
deposito = 0
saque = 0
extratoDeposito = []
extratoSaque = []
total = 0
totalSaque = 0
totalDeposito = 0

while True:
    
    opcao = input(menu)
    
    if opcao == '1':
        while True:
            print("\nDEPÓSITO:")
            print("Valor na conta -> ", saldo)
            print("(Insira 0 p/ cancelar...)")
            deposito = input("Valor inserido: ")
            
            if not deposito.isdigit() or float(deposito) < 0:
                print("Digite um valor válido...")
            elif float(deposito) == 0:
                print("Operação cancelada!")
                break
            else:
                extratoDeposito.append(float(deposito))
                totalDeposito += float(deposito)
                saldo += float(deposito)
                print("Deposito realizado com sucesso!")
                break
    
    elif opcao == '2':
        while True:
            print("\nSAQUE:")
            print("Valor disponível -> ", saldo)
            print("(Insira 0 p/ cancelar...)")
            saque = input("Valor inserido: ")
            
            if not saque.isdigit() or float(saque) < 0:
                print("Digite um valor válido...")
            elif float(saque) == 0:
                print("Operação cancelada!")
                break
            elif float(saque) > float(saldo):
                print("Crédito não disponível!")
            else:
                extratoSaque.append(float(saque))
                totalSaque += float(saque)
                saldo -= float(saque)
                print("Saque realizado com sucesso!")
                break

    elif opcao == '3':
        print("\n====== EXTRATO BANCÁRIO ======")
        print("Depósitos:")
        for i, deposito in enumerate(extratoDeposito, start=1):
            print(i,"-", "R$", deposito)
        print("Saques:")
        for i, saque in enumerate(extratoSaque, start=1):
            print(i,"-", "R$", saque)
        print("TOTAL:")
        print("Depósitos -> ", totalDeposito)
        print("Saques -> ", totalSaque)
        print("Saldo -> ", saldo)
        print("==============================")
        
    elif opcao == '4':
        print("\nSaindo...")
        break
    
    else:
        print("Insira uma opção válida...")