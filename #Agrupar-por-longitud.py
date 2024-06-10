#Agrupar-por-longitud

def agrupar_por_longitud(palabras):
    longitud_palabras = {}
    for palabra in palabras:
        longitud = len(palabra)
        if longitud in longitud_palabras:
            longitud_palabras[longitud].append(palabra)
        else:
            longitud_palabras[longitud] = [palabra]
    return longitud_palabras

# Ejemplo de uso:
palabras = ["Hola", "mundo", "Python", "es", "genial"]
print(agrupar_por_longitud(palabras))
