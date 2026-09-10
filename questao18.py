contador = 0
for i in range(7):
    faturamento = float(input("Digíte o faturamento do dia: "))
    contador+=faturamento
print(f"Faturamento da semana {contador}")