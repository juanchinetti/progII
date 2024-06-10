#Diccionario-de-listas-a-una-lista

def diccionario_a_lista(diccionario):
    resultado = []
    for lista in diccionario.values():
        resultado += lista
    return resultado

# Ejemplo de uso:
diccionario = {"a": [1, 2, 3], "b": [4, 5], "c": [6, 7, 8]}
print(diccionario_a_lista(diccionario))
