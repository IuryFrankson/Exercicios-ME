desempenho_alunos = {}

for i in range(5):
    nome = input(f"Introduza o nome do {i + 1}° aluno: ")
    nota = float(input(f"Introduza a nota de {nome}: "))
    desempenho_alunos[nome] = nota

print("\n===== Registros de Desempenho =====")
for nome, nota in desempenho_alunos.items():
    print(f"Estudante: {nome} - Nota: {nota}")