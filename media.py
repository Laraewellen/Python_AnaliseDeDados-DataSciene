nome = input ("Digite seu nome: ")

Nota1 = float(input("1ª nota: "))
Nota2 = float(input("2ª nota: "))
Nota3 = float(input("3ª nota: "))

media = (Nota1 + Nota2 + Nota3)/3

if media < 7:
    print(f"O aluno {nome} foi reprovado com média {media} ")
else:
    print(f"O aluno {nome} foi aprovado com média {media}")