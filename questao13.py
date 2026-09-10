setor1 = float(input("Digíte o consumo do setor 1 em kWh "))
setor2 = float(input("Digíte o consumo do setor 2 em kWh "))

if setor1==setor2:
    print("O consumo dos setores foi igual ")
elif setor1>setor2:
    print(f"O consumo do setor 1 foi maior. \n Consumo: {setor1}")
else:
    print(f"O consumo do setor 2 foi maior. \n Consumo: {setor2}")