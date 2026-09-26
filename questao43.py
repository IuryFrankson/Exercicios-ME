matriz_dados = [
    [10, 45, 20],
    [64, 85, 32],
    [94, 9, 38]
]

maior_valor = matriz_dados[0][0]

for linha in matriz_dados:
    for valor in linha:
        if valor > maior_valor:
            maior_valor = valor

print(f"O maior valor na matriz é: {maior_valor}.")