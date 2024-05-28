#Encontrar índice:

def encontrar_indice(lista, valor):
    try:
        return lista.index(valor)
    except ValueError:
        return -1


print(encontrar_indice([1, 2, 3, 4, 5], 3))  
print(encontrar_indice([1, 2, 3, 4, 5], 6))  