# Escribir un programa que reciba una cadena de caracteres y
# devuelva un diccionario con cada palabra que contiene y
# su frecuencia. Escribir otra función que reciba el diccionario
# generado con la función anterior y devuelva una tupla
# con la palabra más repetida y su frecuencia.

def conteo_palabras(fragmento):
    """Función que recibe una cadena de caracteres
    y devuelve un diccionario con cada palabra
    que contiene y su frecuencia
    Parámetros:
        -Fragmento: cadena de caracteres
    Salida:
        Diccionario con cada palabra del fragmento
        y su frecuencia
    """
    dict_frecuencias = {}
    lista_palabras = fragmento.split(" ")
    for palabra in lista_palabras:
        if palabra in dict_frecuencias.keys():
            dict_frecuencias[palabra] += 1
        else:
            dict_frecuencias[palabra] = 1
    return dict_frecuencias


def mayor_frecuencia(dict_frecuencias):
    """Función que recibe el diccionario generado por la
    funcion conteo_palabras y devuelve una tupla con la
    palabra más repetida y su frecuencia.
    Parámetro:
        -Diccionario con las palabras del fragmento y
        su frecuencia
    Salida:
        -Tupla con la palabra más repetida y su
        frecuencia
    """
    rep_max = 0
    clave_max = 0
    for palabra, repeticiones in dict_frecuencias.items():
        if repeticiones > rep_max:
            rep_max = repeticiones
            clave_max = palabra
    return (clave_max, rep_max)