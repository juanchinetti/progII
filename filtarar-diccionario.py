#Filtrar diccionario:

def filtrar_diccionario(diccionario, claves):
    return {k: diccionario[k] for k in claves if k in diccionario}

print(filtrar_diccionario({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])) 