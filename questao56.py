def calcular_graos_xadrez():
    total_graos = 0
    for casa in range(64):
        total_graos += 2 ** casa
    return total_graos

resultado = calcular_graos_xadrez()
print(f"O monge esperava receber {resultado} graos de trigo.")