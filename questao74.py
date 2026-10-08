base_de_dados = {"1": "Portatil", "2": "Mouse"}

def rota_produto(produto_id):
    try:
        if produto_id == "999":
            raise ConnectionError("Falha na base de dados")
            
        produto = base_de_dados[produto_id]
        return {"status": 200, "body": produto}
    except KeyError:
        return {"status": 404, "body": "Produto nao encontrado"}
    except Exception:
        return {"status": 500, "body": "Erro interno do servidor"}

# Exemplos
print(rota_produto("1"))
print(rota_produto("3"))
print(rota_produto("999"))