matriz_operacao = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_diagonal = 0

for i in range(len(matriz_operacao)):
    soma_diagonal += matriz_operacao[i][i]

print(f"A soma dos elementos da diagonal principal é: {soma_diagonal}")