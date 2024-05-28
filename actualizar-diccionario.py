#Actualizar diccionario:

def actualizar_diccionario(diccionario, lista_tuplas):
    for clave, valor in lista_tuplas:
        diccionario[clave] = valor
    return diccionario
print(actualizar_diccionario({'a': 1, 'b': 2}, [('b', 3), ('c', 4)])) 
