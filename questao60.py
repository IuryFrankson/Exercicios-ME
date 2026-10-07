def converter_f_para_c(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

try:
    valor_f = float(input("Informe o valor da temperatura em graus Fahrenheit: "))
    resultado_c = converter_f_para_c(valor_f)
    print(f"A temperatura de {valor_f}°F equivale a {resultado_c}°C.")
except ValueError:
    print("Erro: Por favor, insira um valor numerico valido.")