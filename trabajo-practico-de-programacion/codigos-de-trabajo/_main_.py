from producto import Producto
from electronico import Electronico
from Alimento import Alimento

#Crear instancias de las clases hijas
producto_electronico = Electronico("Laptop", 1500.00, 10, "Lenovo", "ThinkPad X1")
producto_alimento = Alimento("Manzanas", 2.50, 100, "2024-06-30")

#Mostrar información de los productos
print("Información del producto electrónico:")
producto_electronico.mostrar_informacion()
print("\nInformación del producto alimenticio:")
producto_alimento.mostrar_informacion()
