# Questao A
class ProdutoInvalidoError(Exception):
    pass
class ValorInvalidoError(Exception):
    pass
class QuantidadeInvalidaError(Exception):
    pass

# Questao B
def registrar_venda(produto, preco, quantidade):
    if not produto or not produto.strip():
        raise ProdutoInvalidoError("Nome do produto vazio.")
    try:
        preco = float(preco)
        if preco <= 0:
            raise ValorInvalidoError("O preco deve ser superior a zero.")
    except ValueError:
        raise ValorInvalidoError("Formato de preco invalido.")
        
    try:
        quantidade = int(quantidade)
        if quantidade <= 0:
            raise QuantidadeInvalidaError("A quantidade deve ser um numero inteiro positivo.")
    except ValueError:
        raise QuantidadeInvalidaError("Formato de quantidade invalido.")
        
    total_compra = preco * quantidade
    return {"produto": produto, "preco": preco, "quantidade": quantidade}, total_compra

# Questao C
def gerar_relatorio(vendas):
    if not vendas:
        print("\nNenhuma venda registrada hoje.")
        return
        
    total_vendas = len(vendas)
    faturamento_total = sum(v["preco"] * v["quantidade"] for v in vendas)
    ticket_medio = faturamento_total / total_vendas
    
    contagem_produtos = {}
    for v in vendas:
        contagem_produtos[v["produto"]] = contagem_produtos.get(v["produto"], 0) + v["quantidade"]
    
    produto_mais_vendido = max(contagem_produtos, key=contagem_produtos.get)
    
    print("\n----- RELATÓRIO DO DIA -----")
    print(f"Quantidade total de vendas: {total_vendas}")
    print(f"Produto mais vendido: {produto_mais_vendido} ({contagem_produtos[produto_mais_vendido]} unidades)")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print(f"Ticket medio por venda: R$ {ticket_medio:.2f}")
    print("-------------------------")

# Programa principal
def main():
    vendas_validas = []

    while True:
        produto = input("Introduza o nome do produto (ou 'fim' para encerrar): ")
        if produto.lower() == "fim":
            break
            
        preco = input("Introduza o preco unitario: ")
        quantidade = input("Introduza a quantidade vendida: ")
        
        try:
            dados_venda, total = registrar_venda(produto, preco, quantidade)
        except (ProdutoInvalidoError, ValorInvalidoError, QuantidadeInvalidaError) as e:
            print(f"Erro de validacao: {e}\n")
        except Exception as e:
            print(f"Erro inesperado: {e}\n")
        else:
            vendas_validas.append(dados_venda)
            print(f"Venda registrada com sucesso! Total da compra: R$ {total:.2f}")
        finally:
            print("Processamento do pedido concluido.\n")
            
    gerar_relatorio(vendas_validas)