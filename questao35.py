estoque = {
    "Hashis de cerâmica": 27,
    "Descanso de copo": 44,
    "Copos de cristal": 31
}

print("===== Estoque Atual =====")
for produto, quantidade in estoque.items():
    print(f"{produto.capitalize()}: {quantidade} unidades")