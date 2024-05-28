#Diccionario de frecuencias

def diccionario_frecuencias(lista_palabras):
    frecuencia = {}
    for palabra in lista_palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
print(diccionario_frecuencias(['hola', 'sapo', 'code', 'milanesa'])) 