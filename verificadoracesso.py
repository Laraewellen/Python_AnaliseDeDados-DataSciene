
Nome = input("Usuário: ")

Senha = input("Senha: ")

senhacerta = '1234'

if Senha == senhacerta:
    print(f"Bem vindo(a) {Nome}")
    try: 
        Idade = int (input("Digite sua idade: "))

        if Idade < 0:
            print("Idade inválida")

        elif Idade < 18:
            print(f"Acesso negado, é nescessário ter no mínimo 18 anos")

        else:
            print(f"Acesso autorizado, bem vindo(a) {Nome}")
    except ValueError:
        print("Somente números são válidos para a idade")
else:
    print("Senha errada!")
