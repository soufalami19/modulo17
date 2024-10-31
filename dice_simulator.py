import dice
import time

def lanzar_dados(amount, sides):
    resultados = [dice.roll(f'1d{sides}') for _ in range(amount)]
    for i, resultado in enumerate(resultados, start=1):
        print(f"Lanzamiento {i} número obtenido {resultado}")
        time.sleep(5)
    return resultados

lanzar_dados(amount=6, sides=6)

