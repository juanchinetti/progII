#Elementos mayores que un valor:

def elementos_mayores(lista, n):
    return [x for x in lista if x > n]


print(elementos_mayores([1, 2, 3, 4, 5], 3))  