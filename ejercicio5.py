# Escribir una función que reciba una muestra de números
# en una lista y devuelva otra lista con sus cuadrados.

def cuadrados(numeros):
    """Función que recibe una lista de números
    y devuelve otra lista con sus cuadrados.
    Parámetros:
        -Numeros: Lista de números
    Salida:
         Lista con los números al cuadrado
    """
    lista_cuadrados = []
    for numero in numeros:
        numero = numero ** 2
        lista_cuadrados.append(numero)
    return lista_cuadrados


print(cuadrados([2, 4, 1, 5]))
