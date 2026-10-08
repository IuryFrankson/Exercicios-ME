def realizar_saque(saldo, valor_saque):
    if valor_saque <= 0:
        raise ValueError("O valor do saque deve ser positivo.")
    if valor_saque > saldo:
        raise ValueError("Saldo insuficiente.")
    return saldo - valor_saque

saldo_conta = 500.0
try:
    valor_desejado = float(input("Introduza o valor do saque: "))
    saldo_conta = realizar_saque(saldo_conta, valor_desejado)
    print(f"Saque efetuado. Novo saldo: {saldo_conta:.2f}")
except ValueError as e:
    print(f"Erro na operacao: {e}")