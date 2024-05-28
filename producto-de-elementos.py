#Producto de elementos:

def producto_elementos(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

print(producto_elementos([1, 2, 3, 4, 5]))  