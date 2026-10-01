for i in range(5):
    while True:
        try: 
            numeros = float(input(f"Digite o {i + 1}° numero: "))
        except ValueError:
            print("Digite um valor numerico valido.")

#acho que tá errado mas depois arrumo e termino