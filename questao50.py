nota_alunos = {

}

contador = 0

while contador <=4:
    nome_aluno = input("Digíte o nome do aluno: ")
    nota_aluno = float(input("Digíte a nota do aluno: "))
    nota_alunos[nome_aluno] = nota_aluno
    contador+=1
    print(nota_alunos)

media = sum(nota_alunos.values()) / len(nota_alunos)

for nome,nota in nota_alunos.items():
    if nota>=7:
        print("Aluno aprovado: ", nome)
        print("\t Nota do aluno: ", nota)

#1,2,4,5,6,9,11,27,54