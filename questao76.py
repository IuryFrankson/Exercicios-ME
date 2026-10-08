import traceback

dados = [10, "20", "abc", None, 30]

def processar_dados(dados):
    for item in dados:
        try:
            numero = int(item)
            resultado = numero ** 2
            print(f"O quadrado de {numero} eh {resultado}")
        except (TypeError, ValueError) as e:
            print(f"\nErro ao processar o item '{item}':")
            traceback.print_exc() 
            print("-" * 40)