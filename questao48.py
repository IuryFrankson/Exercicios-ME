ordem = 3
matriz_identidade = []

for i in range(ordem):
    linha = []
    for j in range(ordem):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
        matriz_identidade.append(linha)

print('Matriz Identidade de Ordem 3:')
for linha in matriz_identidade:
    print(linha)