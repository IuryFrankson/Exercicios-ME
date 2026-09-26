funcionario = {
    "nome": "Layla Menezes",
    "idade": "22",
    "setor": "Design Web"
}

print("===== Dados do Funcionário =====")
for chave, valor in funcionario.items():
    print(f"{chave.capitalize()}: {valor}")