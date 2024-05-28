#Valores únicos:

def valores_unicos(diccionario):
    return list(set(diccionario.values()))
print(valores_unicos({'a': 1, 'b': 2, 'c': 1}))