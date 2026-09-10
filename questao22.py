qt_alunos = int(input("Digíte a quantidade de alunos: "))
lista_notas = []
for i in range(1, qt_alunos+1):
    nota = float(input(f"Digíte a nota do aluno {i}: "))
    lista_notas.append(nota)
print(max(lista_notas))
