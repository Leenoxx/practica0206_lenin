# Escribir una función que reciba un número entero positivo
# y devuelva su factorial. Realiza el ejercicio mediante
# bucles interactivos y mediante una función recursiva.

def factorial(n):
    """Función que devuelve el factorial de un numero introducido.

    Parámetros:
        -n: número real para calcular el factorial
    Salida:
        Factorial del número introducido
    """
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def factorial_recursivo(n):
    """Función que devuelve el factorial de un numero introducido
    realizado con una función recursiva.

    Parámetros:
        -n: número real para calcular el factorial
    Salida:
        Factorial del número introducido
    """
    if n == 1:
        fact = 1
    else:
        fact = n * factorial_recursivo(n-1)
    return fact


numero = int(input("Introduce un número: "))

print(factorial(numero))
print(factorial_recursivo(numero))
