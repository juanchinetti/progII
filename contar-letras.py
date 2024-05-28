
#Contar letras:


def contar_letras(cadena):
    frecuencia = {}
    for letra in cadena:
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            frecuencia[letra] = 1
    return frecuencia

print(contar_letras("hola mundo")) 
