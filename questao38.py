import random

lista_livros = [
    "O Pequeno Príncipe",
    "1984",
    "Harry Potter e a Pedra Filosofal",
    "Ordem Paranormal",
    "O Diário de Anne Frank"
]

livro_indicado = random.choice(lista_livros)

print(f"O livro indicado é: '{livro_indicado}'.")