def Calcular_Promedio(lista):
    Suma = sum(lista)
    promedio = Suma / len(lista)
    return promedio

numeros = [5,8,10,3,9]
print("El Promedio de la Lista es:", Calcular_Promedio(numeros)) 