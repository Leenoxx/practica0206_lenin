# Escribir una función que convierta un número decimal
# en binario y otra que convierta un número binario en decimal.

def convertir_binario(decimal):
    """Función que recibe un número decimal y
    lo convierte a binario
    Parámetros:
        -decimal: Número decimal real
    Salida:
         Número binario del decimal introducido
    """
    lista_binario = []
    if decimal == 0:
        print(0)
    else:
        while decimal != 0:
            a = decimal % 2
            lista_binario.append(int(a))
            if a == 1:
                decimal = decimal / 2
                decimal = decimal - 0.5
            else:
                decimal = decimal / 2
        lista_binario.reverse()
        for i in lista_binario:
            print(i, end="")
    return ""


def convertir_decimal(num_binario):
    """Función que recibe un número binario
    y devuelve el numero decimal equivalente.
    Parametro:
        -num_binario: número en forma binaria
    Salida:
         Número real en forma decimal
    """
    lista = []
    lista_decimal = []
    for i in str(num_binario):
        lista.append(i)
    lista.reverse()
    numero = 0
    numero_decimal = 0
    for cifra in lista:
        binario = int(cifra) * (2 ** numero)
        lista_decimal.append(binario)
        numero += 1
    for x in lista_decimal:
        numero_decimal = numero_decimal + int(x)
    return numero_decimal
