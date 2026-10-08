def cadastrar_produto(nome, preco, quantidade):
    if not nome or not nome.strip():
        raise ValueError("O nome do produto nao pode estar vazio.")
    if preco <= 0:
        raise ValueError("O preco do produto deve ser maior que zero.")
    if quantidade < 0:
        raise ValueError("A quantidade nao pode ser negativa.")
    
    return "Produto registrado com sucesso!"

try:
    mensagem = cadastrar_produto("Teclado", 45.99, 10)
    print(mensagem)
except ValueError as e:
    print(f"Erro ao registar: {e}")