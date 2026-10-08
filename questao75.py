import random
import time

def mock_api_connect():
    if random.random() < 0.7:
        raise ConnectionError("Falha na ligacao com a API de terceiros.")
    return "Ligacao bem-sucedida!"

def conectar_com_tentativas(max_tentativas = 3):
    tentativas = 0
    while tentativas < max_tentativas:
        try:
            tentativas += 1
            print(f"Tentativa {tentativas} de {max_tentativas}...")
            resultado = mock_api_connect()
            print(resultado)
            return
        except ConnectionError as e:
            print(f"Aviso: {e}")
            time.sleep(1)
            
    print("Falha critica: O limite de tentativas foi atingido. A encerrar de forma segura.")