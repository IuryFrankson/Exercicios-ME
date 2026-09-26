import random

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("Bem-vindo à competição! Tente adivinhar o número entre 1 e 100.")

while not acertou:
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você adivinhou o número em {tentativas} tentativa(s).")
        acertou = True
    elif palpite < numero_secreto:
        print("Incorreto. O número procurado é MAIOR.")
    else:
        print("Incorreto. O número procurado é MENOR.")