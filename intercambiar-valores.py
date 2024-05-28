#Intercambiar valores:

def intercambiar_valores(diccionario, clave1, clave2):
    diccionario[clave1], diccionario[clave2] = diccionario[clave2], diccionario[clave1]
    return diccionario
print(intercambiar_valores({'a': 1, 'b': 2, 'c': 3}, 'a', 'c')) 
