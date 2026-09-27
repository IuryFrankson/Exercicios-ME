estoque = {}

print("===== Cadastro de medicamentos =====")
for i in range(5):
    nome = input(f"Nome do {i + 1}° medicamento: ")
    qtd = int(input(f"Quantidade de {nome}: "))
    estoque[nome] = qtd

busca = input("\nIntroduza o nome do medicamento para consultar o estoque: ")
quantidade = estoque.get(busca)

if quantidade is not None:
    print(f"Quantidade disponível em estoque: {quantidade}")
else:
    print("Medicamento não encontrado.")