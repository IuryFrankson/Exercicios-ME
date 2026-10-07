def ler_relatorio():
    arquivo = None
    try:
        arquivo = open('relatorio_vendas.txt', 'r')
        dados = arquivo.read()
        print(dados)
    except FileNotFoundError:
        print("Erro: O arquivo 'relatorio_vendas.txt' não foi encontrado no sistema.")
    finally:
        print("Operacao finalizada. Encerrando o recurso de arquivo.")
        if arquivo:
            arquivo.close()