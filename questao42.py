matriz_producao = [
    [150, 200, 100],
    [300, 50, 230]
]

soma_total = 0

for linha in matriz_producao:
    for valor in linha:
        soma_total += valor

print(f"A soma dos valores de produção é: {soma_total}.")