precos = ["100.00", "50.00", "invalido", "200.00"]

for preco in precos:
    try:
        preco_float = float(preco)
    except ValueError:
        print(f"Erro: Nao foi possivel converter '{preco} para numero.")
    else:
        preco_com_desconto = preco_float *0.90
        print(f"Preco original: {preco_float:.2f} | Com desconto: {preco_com_desconto:.2f}")