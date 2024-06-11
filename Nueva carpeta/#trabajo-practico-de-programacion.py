#trabajo-practico-de-programacion-(producto)

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

class Producto:
    def __init__(self, nombre, precio, cantidad):
        """
        Constructor de la clase Producto.

        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        :param cantidad: Cantidad disponible del producto.
        """
        # Inicializa el atributo nombre del producto
        self.nombre = nombre
        # Inicializa el atributo precio del producto
        self.precio = precio
        # Inicializa el atributo cantidad disponible del producto
        self.cantidad = cantidad

    def mostrar_informacion(self):
        """
        Muestra la información básica del producto.
        """
        # Imprime el nombre del producto
        print(f"Nombre: {self.nombre}")
        # Imprime el precio del producto
        print(f"Precio: ${self.precio}")
        # Imprime la cantidad disponible del producto
        print(f"Cantidad: {self.cantidad} unidades")