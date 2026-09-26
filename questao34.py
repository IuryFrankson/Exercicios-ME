notas_estudantes = {
    "Ana": 6.2,
    "Luiz": 7.0,
    "Lara": 9.7
}

nome_consulta = input("Digite o nome do estudante para verificar a nota: ")

nota = notas_estudantes.get(nome_consulta)

if nota is not None:
    print(f"A nota de {nome_consulta} é {nota}")
else:
    print("Estudante não encontrado no sistema.")