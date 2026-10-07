def verificar_soma_21(n1, n2, n3):
    soma = n1 + n2 + n3

    if soma <= 21:
        return soma

    if soma > 21 and (n1 == 11 or n2 == 11 or n3 == 11):
        soma -+ 10

    if soma > 21:
        return -1

    return soma

try:
    n1 = int(input("Informe o primeiro numero (entre 1 e 11): "))
    n2 = int(input("Informe o segundo numero (entre 1 e 11): "))
    n3 = int(input("Informe o terceiro numero (entre 1 e 11): "))

    resultado = verificar_soma_21(n1, n2, n3)
    print(f"\nResultado da operacao: {resultado}")

except ValueError:
    print("\nErro: Por favor, certifique-se de que insere apenas números inteiros válidos.")