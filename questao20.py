contador = 0
while True:
    nota = float(input("Digíte a nota: "))
    contador+=nota
    continuacao = int(input("Digíte 0 para parar a coleta ou 1 para continuar: "))
    if continuacao==0:
        break
print(contador)