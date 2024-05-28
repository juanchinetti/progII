#Diccionario de cuadrados:

def diccionario_cuadrados(n):
    return {i: i**2 for i in range(1, n+1)}
print(diccionario_cuadrados(5)) 