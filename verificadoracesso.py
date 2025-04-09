
Nome = input("Usuário: ")

Senha = input("Senha: ")

senha_correta = "1234"

while Senha != senha_correta:
    print("Senha incorreta, tente novamente")
    Senha = input("senha: ")
    
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

