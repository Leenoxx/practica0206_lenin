# Escribir una función a la que se le pase una cadena <nombre> y
# muestre por pantalla el saludo ¡hola <nombre>!.

def saludo(nombre):
    """Función que devuelve un saludo con un nombre.

    Parámetros:
        -nombre: cualquier palabra o nombre de persona
    Salida:
        Imprime un "¡hola <nombre>!, siendo <nombre> la palabra que se introduce.
    """
    print("¡hola", nombre, end="!")
    return

saludo("Samuel")
