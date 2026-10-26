print("ola seja bem vindo ao sistema de senha")
nome = input("Digite seu nome: ")
senha = input("coloque sua senha: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("ola", nome, "voce tem acesso ao sistema")
    input_senha = input("Digite sua senha para entrar: ")

    if input_senha == senha:
        print("Senha correta! Acesso concedido.")

        while True:
            oque_vamos_agora = (
                input(
                    "\nO que vamos fazer agora? (calculadora / par ou impar / sair): "
                )
                .strip()
                .lower()
            )

            if oque_vamos_agora == "calculadora":
                n1 = float(input("Digite o primeiro numero: "))
                n2 = float(input("Digite o segundo numero: "))
                operacao = input("Digite a operação (+, -, *, /): ").strip()

                if operacao == "+":
                    print("O resultado da soma é:", n1 + n2)
                elif operacao == "-":
                    print("O resultado da subtração é:", n1 - n2)
                elif operacao == "*":
                    print("O resultado da multiplicação é:", n1 * n2)
                elif operacao == "/":
                    if n2 != 0:
                        print("O resultado da divisão é:", n1 / n2)
                    else:
                        print("Erro: Divisão por zero não é permitida.")
                else:
                    print("Operação inválida!")

            elif oque_vamos_agora == "par ou impar":
                num = int(input("Digite um numero: "))
                if num % 2 == 0:
                    print(f"O numero {num} é PAR")
                else:
                    print(f"O numero {num} é ÍMPAR")

            elif oque_vamos_agora == "sair":
                print("Saindo do sistema... Até logo!")
                break

            else:
                print("Opção inválida! Escolha 'calculadora', 'par ou impar' ou 'sair'.")

    else:
        print("Senha incorreta! Acesso negado.")
else:
    print("Desculpe", nome, "voce nao tem acesso ao sistema")
