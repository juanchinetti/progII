#Contar letras:

def diccionario_inverso(diccionario):
    inverso = {}
    for k, v in diccionario.items():
        inverso[v] = k
    return inverso


print(diccionario_inverso({'a': 1, 'b': 2, 'c': 3}))  
