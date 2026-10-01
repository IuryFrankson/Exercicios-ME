num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if num1 and num2 %2 == 0:
    if num1 < num2:
        print(f"O menor numero foi {num1}")
    elif num2 < num1:
        print(f"O menor numero foi {num2}")
else:
    if num1 > num2:
        print(f"O maior numero foi {num1}")
    elif num2 > num1:
        print(f"O maior numero foi {num2}")