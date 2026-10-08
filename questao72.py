def parse_cpf(cpf):
    if not isinstance(cpf, str) or len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("Formato de CPF invalido. O CPF deve conter exatamente 11 digitos.")
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def main():
    cpf_usuario = int(input("introduza o seu CPF (apenas numeros): "))
    try:
        cpf_formatado = parse_cpf(cpf_usuario)
        print(f"CPF valido: {cpf_formatado}")
    except ValueError as e:
        print(f"Erro ao processar utilizador: {e}")