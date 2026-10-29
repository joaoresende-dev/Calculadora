print("-" * 10 + " bem vindo a calculadora " + "-" * 10)

nome = input("digite seu nome: ")
print("seja bem vindo, " + nome)

senha_1 = input("digite a sua senha: ")
senha_2 = input("confirme a sua senha: ")

while senha_1 != senha_2:
    print("senha incorreta, tente novamente")
    senha_1 = input("digite a sua senha: ")
    senha_2 = input("confirme a sua senha: ")

print("senha correta, você pode acessar a calculadora")

while True:
    print("\n" + "=" * 40)
    print("na calculadora temos as seguintes opções:")
    print("digite (1) 🖩 para a calculadora 🖩")
    print("digite (2) para impar ou par")
    print("digite (3) para sair do programa")
    
    opção = input("digite sua opção: ")

    try:
        if opção == "1":
            print("🖩 você escolheu calculadora 🖩")
            n1 = float(input("digite seu primeiro numero: ").replace(",", "."))
            n2 = float(input("digite seu segundo numero: ").replace(",", "."))

            print("digite (+) para somar")
            print("digite (-) para subtrair")
            print("digite (*) para multiplicar")
            print("digite (/) para dividir")
            opção_calculadora = input("digite a sua operação: ")

            if opção_calculadora == "+":
                print("resultado é:", n1 + n2)

            elif opção_calculadora == "-":
                print("resultado é:", n1 - n2)

            elif opção_calculadora == "*":
                print("resultado é:", n1 * n2)

            elif opção_calculadora == "/":
                if n2 != 0:
                    print("resultado é:", n1 / n2)
                else:
                    print("Erro: não é possível dividir por zero!")
            else:
                print("Operação inválida!")

        elif opção == "2":
            print("você escolheu par e ímpar")
            n3 = int(input("digite seu número para saber se é ímpar ou par: "))
            
            if n3 % 2 == 0:
                print("o número", n3, "é par")
            else:
                print("o número", n3, "é ímpar")

        elif opção == "3":
            print("você escolheu sair. tchau!")
            break

        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")

    except ValueError:
        print("Erro: digite apenas números válidos!")
