def dividir_lucros():
    try:
        lucro_total = float(input("Informe o lucro total do trimestre: "))
        quantidade_acionistas  = int(input("Informe a quantidade de acionistas: "))

        lucro_individual = lucro_total / quantidade_acionistas
        print(f"Cada acionista recebera: R${lucro_individual:.2f}")

    except ValueError:
        print("Erro: Os dados informados devem ser numeros validos.")
    except ZeroDivisionError:
        print("Erro: Não eh possivel dividir os lucros entre zero acionistas.")