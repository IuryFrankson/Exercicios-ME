temperaturas = []

for i in range(1, 6):
    temp = float(input(f"Introduza a temperatura do dia {i}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)

print(f"\nTemperaturas registradas: {temperaturas}")
print(f"Média das temperaturas: {media:.2f}°C")

if 18 <= media <= 28:
    print("A média está dentro da faixa ideal de cultivo.")
else:
    print("A média está fora da faixa ideal de cultivo.")