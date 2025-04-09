import random

numero_secreto = random.randint(1,100) #sorteia um numero de 1 a 100

tentativas = 0

while True:
    palpite = input ("Adivinhe o numero entre 1 e 100: ")

    if not palpite.isdigit(): #para que a pessoa não use letras
        print("Digite apenas números!")
        continue

    palpite = int(palpite) #converte texto para inteiro

    tentativas += 1 #soma 1 ao numero de tentativas

    if palpite < numero_secreto:
        print("O número é maior que esse")

    elif palpite > numero_secreto:
        print("O numero é menor que esse")

    else:
        print("Parabéns, você acertou!!!")
        print(f"Foram um total de {tentativas} tentativas")
        break