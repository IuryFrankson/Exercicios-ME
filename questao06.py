codigo = int(input("Digite o código do equipamento: "))

if codigo % 2 == 0:
    print("Equipamento pertencente ao setor administrativo.")
else:
    print("Equipamento pertencente ao setor operacional.")