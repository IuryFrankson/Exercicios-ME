estacionamento = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

vagasOcupadas = 0
vagasLivres = 0

for linha in estacionamento:
    for vaga in linha:
        if vaga == 1:
            vagasOcupadas += 1
        elif vaga == 0:
            vagasLivres += 1

print(f"Total de vagas ocupadas: {vagasOcupadas}")
print(f"Total de vagas disponíveis: {vagasLivres}")