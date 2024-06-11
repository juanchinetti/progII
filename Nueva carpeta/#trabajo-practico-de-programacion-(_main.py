#trabajo-practico-de-programacion-(_main_)

"""
    
    Detalles del Ejercicio
1. Definir la clase Producto:
○ La clase Producto debe tener los siguientes atributos:
■ nombre: El nombre del producto.
■ precio: El precio del producto.
■ cantidad: La cantidad disponible del producto.
○ La clase Producto debe tener un método para mostrar la información del producto.

2. Definir dos clases hijas:
○ Electronico:
■ Atributos adicionales: marca, modelo.
■ Método para mostrar la información específica del producto electrónico.
○ Alimento:
■ Atributos adicionales: fecha_expiracion.
■ Método para mostrar la información específica del producto alimenticio.

3. Implementar las clases:
○ Cada clase hija debe llamar al constructor de la clase Producto para inicializar los atributos
heredados.
○ Cada clase hija debe tener un método para mostrar la información completa del producto,
incluyendo los atributos específicos de la clase hija.
    
"""

#Importamos las clases Electronico y Alimento desde sus respectivos archivos.
from electronico import Electronico
from alimento import Alimento

#Crear una instancia de la clase Electronico con los atributos específicos.
monitor = Electronico(nombre="monitor", precio=600.00, cantidad=12, marca="HP", modelo="SQL32C")

#Crear una instancia de la clase Alimento con los atributos específicos.
peras = Alimento(nombre="peras", precio=5.00, cantidad=200, fecha_expiracion="2024-08-29")

#Mostrar la información del producto electrónico llamando al método mostrar_informacion.
print(monitor.mostrar_informacion())

#Mostrar la información del producto alimenticio llamando al método mostrar_informacion.
print(peras.mostrar_informacion())