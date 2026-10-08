class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem="Saldo insuficiente para efetuar o saque."):
        super().__init__(mensagem)

def realizar_saque(saldo_atual, valor_saque):
    saldo_atual = float(input("Insira o valor do seu saldo atual: "))
    valor_saque = float(input("Insira o valor que deseja sacar: "))
    if valor_saque > saldo_atual:
        raise SaldoInsuficienteError(f"Tentativa de sacar {valor_saque} excedeu o saldo de {saldo_atual}.")
    saldo_atual -= valor_saque
    return saldo_atual