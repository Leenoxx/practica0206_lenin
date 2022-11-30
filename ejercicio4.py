# Escribir una función que reciba una muestra de
# números en una lista y devuelva su media.

def media(numeros):
    """Función que devuelve la media de una lista
    de numeros introducida.
    Parametros:
        -Numeros: lista que se introduce
    Salida:
        Media de los numeros de la lista
    """
    media = 0
    cont = 0
    for numero in numeros:
        media = media + numero
        cont += 1
    return media / cont


print(media([2, 5, 7, 1, 8]))
