matriz_pesquisa = [
    [-6, 5, 0],
    [12, -1, 8],
    [-2, -3, 4]
]

contagem_positivos = 0

for linha in matriz_pesquisa:
    for valor in linha:
        if valor > 0:
            contagem_positivos += 1

print(f"Existem {contagem_positivos} valores positivos na matriz.")