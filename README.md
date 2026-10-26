# sistema-de-acesso
# Projeto em Python com validação de acesso/senha, calculadora e verificador de par ou ímpar.
print("=== SISTEMA DE ACESSO ===")
nome = input("Digite seu nome: ")
senha = input("Crie sua senha: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("\nOlá,", nome, "! Acesso liberado.")
    input_senha = input("Digite sua senha para entrar: ")

    if input_senha == senha:
        print("Senha correta! Bem-vindo ao painel.")

        while True:
            print("\n=========================")
            print("      MENU PRINCIPAL      ")
            print("=========================")
            print("[ 1 ] Calculadora")
            print("[ 2 ] Par ou Ímpar")
            print("[ 3 ] Sair")
            print("=========================")

            opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()

            if opcao == "1":
                print("\n--- CALCULADORA ---")
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
                operacao = input("Digite a operação (+, -, *, /): ").strip()

                if operacao == "+":
                    print("Resultado:", n1 + n2)
                elif operacao == "-":
                    print("Resultado:", n1 - n2)
                elif operacao == "*":
                    print("Resultado:", n1 * n2)
                elif operacao == "/":
                    if n2 != 0:
                        print("Resultado:", n1 / n2)
                    else:
                        print("Erro: Divisão por zero!")
                else:
                    print("Operação inválida!")

            elif opcao == "2":
                print("\n--- PAR OU ÍMPAR ---")
                num = int(input("Digite um número: "))
                if num % 2 == 0:
                    print("O número", num, "é PAR.")
                else:
                    print("O número", num, "é ÍMPAR.")

            elif opcao == "3":
                print("\nSaindo do sistema... Até logo!")
                break

            else:
                print("\nOpção inválida! Digite apenas 1, 2 ou 3.")

    else:
        print("Senha incorreta! Acesso negado.")
else:
    print("Desculpe,", nome, ". Você é menor de idade e não tem acesso.")
