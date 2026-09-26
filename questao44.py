matriz_custos = [
    [10, 45, 20],
    [64, 85, 32],
    [94, 9, 38]
]

menor_valor = matriz_custos[0][0]

for linha in matriz_custos:
    for valor in linha:
        if valor < menor_valor:
            menor_valor = valor

print(f"O menor custo é: {menor_valor}.")