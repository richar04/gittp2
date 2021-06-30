import random


def jugar(cantidad_fichas, cantidad_apuestas):
    lista = [0, 1]
    contador = 0
    while cantidad_fichas > 0 and contador < cantidad_apuestas:
        """print(f"Jugando {contador + 1}")"""
        resultado = random.choices(lista, weights=(0.6, 0.4))
        if resultado == [1]:
            cantidad_fichas += 1
        else:
            cantidad_fichas -= 1
        contador += 1
    print(
        f"Apostaste {contador} veces y te quedaste con un total de {cantidad_fichas} fichas")


for x in range(20):
    jugar(50, 300)
