def menu():
    print("\n========== Calculadora ==========")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção entre 1 a 5: ")

    if opcao in ["1", "2", "3", "4"]:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: você digitou algo que não é número!")
            continue

        if opcao == "1":
            resultado = numero1 + numero2
            print(f"Resultado da soma: {resultado}")

        elif opcao == "2":
            resultado = numero1 - numero2
            print(f"Resultado da subtração: {resultado}")

        elif opcao == "3":
            resultado = numero1 * numero2
            print(f"Resultado da multiplicação: {resultado}")

        elif opcao == "4":
            if numero2 != 0:
                resultado = numero1 / numero2
                print(f"O resultado da divisão é: {resultado}")
            else:
                print("Não é possível dividir por zero!")

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Erro: opção inválida.")
