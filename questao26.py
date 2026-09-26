codigos_produtos = [101, 204, 305, 409, 512]
busca = int(input("Digite o código do produto: "))

if busca in codigos_produtos:
    print("Código encontrado no sistema.")
else:
    print("Código não cadastrado.")