#Contar palabras en frases

def contar_palabras(frases):
    frecuencia_palabras = {}
    for frase in frases:
        palabras = frase.split()
        for palabra in palabras:
            palabra = palabra.lower()
            if palabra in frecuencia_palabras:
                frecuencia_palabras[palabra] += 1
            else:
                frecuencia_palabras[palabra] = 1
    return frecuencia_palabras

# Ejemplo de uso:
frases = ["Hola mundo", "Mundo de Python", "Hola de nuevo"]
print(contar_palabras(frases))
