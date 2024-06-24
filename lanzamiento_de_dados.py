import dice
import time

def lanzar_dados(amount, sides):
    resultados = []
    for i in range(amount):
        resultado = dice.roll(f'1d{sides}')
        resultados.append(resultado)
        print(f"Lanzamiento {i+1}: número obtenido {resultado}")
        time.sleep(5)
    return resultados

# Llamada a la función con amount=5 y sides=6
lanzar_dados(5, 6)
