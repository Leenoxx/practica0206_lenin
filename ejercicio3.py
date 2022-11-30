# Escribir una función que calcule el área de un círculo y
# otra que calcule el volumen de un cilindro usando la primera función.

def area_circulo(radio):
    """Función en el que se introduce un radio de un
    círculo     y devuelve el área de este.
    Parámteros:
        - radio: número real, expresado en metros,
         del radio del círculo
    Salida:
        Cálculo del área del circulo expresado en
        metros
    """
    area = 3.14 * (radio ** 2)
    return area


def volumen_cilindro(area, altura):
    """Función que calcula el volumen de un cilindro
    introduciendo el area de la base y la altura.
    Parametros:
        -altura: numero real expresado en metros de
        la altura del cilindro
    Salida:
        Volumen del cilindro expresado en metros
    """
    volumen = area * altura
    return volumen


print(area_circulo(5))
print(volumen_cilindro(area_circulo(5), 5))
