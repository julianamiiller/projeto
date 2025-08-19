saldo = 1500

print("Caixa eletrônico")
input("Insira o cartão: ")

senhacorreta = "1234"

for tentativa in range(3):

    senha = input("Digite sua senha: ")

    if senha == senhacorreta:
        valor = float(input("Digite o valor para o saque: "))

        if valor <= saldo:
            print(f"O saque do valor {valor} realizado com sucesso.")

            saldo -= valor
            print(f"Saldo restante {saldo}")

        else:
            print("Saldo insuficiente.")
        break 
    
    else:
        print(f"Senha incorreta. Tentativa {tentativa + 1} de 3.")
else:

    print("Número máximo de tentativas excedido. Cartão bloqueado.")

print("Obrigado por usar o caixa eletrônico. Até a próxima!")


