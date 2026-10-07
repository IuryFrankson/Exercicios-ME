def buscar_permissao(dados_acesso, nome_perfil, indice_permissao):
    try:
        lista_permissoes = dados_acesso[nome_perfil]
        return lista_permissoes[indice_permissao]
    except (KeyError, IndexError):
        return "acesso_restrito"

banco_dados = {"admin": ["ler", "escrever", "deletar"], "convidado": ["ler"]}
print(buscar_permissao(banco_dados, "admin", 5))