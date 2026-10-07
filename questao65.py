def calcular_cubo(numero):
    return numero ** 3

def calcular_divisao_cubo(numero):
    if numero % 3 == 0:
        return calcular_cubo(numero)
    return False

print("Teste com o numero 6:", calcular_divisao_cubo(6))
print("Teste com o numero 4:", calcular_divisao_cubo(4))