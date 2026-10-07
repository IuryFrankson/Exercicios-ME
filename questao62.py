def numero_perfeito(numero):
    if numero < 2:
        return False

    soma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i

    return soma_divisores == numero

try:
    numero_informado = int(input("Informe um numero para verificar se eh perfeito: "))

    if numero_perfeito(numero_informado):
        print(f"O numero {numero_informado} eh um numero perfeito!")
    else:
        print(f"O numero {numero_informado} nao eh um numero perfeito.")
except ValueError:
    print("Erro: Por favor, insira um numero inteiro valido.")