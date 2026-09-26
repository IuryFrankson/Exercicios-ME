livro = {
    "titulo": "O Pequeno Príncipe",
    "autor": "Antoine de Saint-Exupéry",
    "ano_publicacao": 1943,
    "disponivel": True
}

print("Informações cadastradas no sistema:")
for chave in livro.keys():
    print("-", chave)