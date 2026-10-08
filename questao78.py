def calcular_media(n1, n2, n3):
    try:
        n1, n2, n3 = float(n1), float(n2), float(n3)
    except ValueError:
        raise ValueError("As entradas devem ser valores numericos.")

    if not (0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10):
        raise ValueError("As notas devem estar no intervalo de 0 a 10.")
    
    media = (n1 + n2 + n3) / 3
    
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperacao"
    else:
        situacao = "Reprovado"
        
    return media, situacao

try:
    media_aluno, estado = calcular_media("8", "7.5", "9")
    print(f"Media: {media_aluno:.2f} - Situacao: {estado}")
except ValueError as e:
    print(f"Erro: {e}")