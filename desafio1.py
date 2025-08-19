saldo = 3000

print("Caixa eletronico ")
input("insira o cartão: ")

senha = input("Digite sua senha: ")

if senha == "1234":
    valor = float(input("Digite o valor para o saque: "))

    if valor <= saldo:
        print(f"O saque do valor {valor} realizado com sucesso. ")
        saldo -= valor
        print(f"Saldo restante {saldo}")
    else: 
        print("Saldo insuficiente. ")
else:
    print("Senha incorreta. ")

print("Obrigado por usar o caixa eletrônico. Até a próxima! ")