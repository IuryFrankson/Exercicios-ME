def contar_animais(total_cabecas, total_pernas):
    coelhos = (total_pernas - (2 * total_cabecas)) / 2
    galinhas = total_cabecas - coelhos

    return int(coelhos), int(galinhas)

coelhos, galinhas = contar_animais(35, 94)
print(f"Seu Chico tem {coelhos} coelhos e {galinhas} galinhas.")