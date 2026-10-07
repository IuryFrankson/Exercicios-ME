def cadastrar_idade():
    while True:
        try:
            idade = int(input("Informe a idade do usuário: "))

            if idade < 0:
                print("A idade nao pode ser um valor negativo. Tente novamente.")
                continue
            
            print(f"Idade {idade} cadastradacom sucesso!")
            break

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")