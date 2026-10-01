materias = ("matematica", "portugues")

nome = input("Digite o seu nome: ")
notaMat = float(input("Digite sua nota de matematica: "))
notaPort = float(input("Digite sua nota de portugues: "))

media = (notaMat + notaPort) / 2

if media >= 7:
    print(f"Parabens {nome}! Voce foi aprovado com a media de {media}!")
else:
    print(f"Estude mais, {nome}. Voce foi reprovado com a media de {media}.")

print(f"Materias cadastradas: {materias}" )