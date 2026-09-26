import random

numero_secreto = random.randint(1, 10)
palpite = int(input("Adivinhe o número entre 1 e 10: "))

if palpite == numero_secreto:
    print("Parabéns! Você acertou o número!")
else:
    print(f"Que pena! Você errou. O número sorteado foi {numero_secreto}.")