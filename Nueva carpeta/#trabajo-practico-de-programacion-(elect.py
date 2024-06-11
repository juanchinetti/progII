#trabajo-practico-de-programacion-(electronico)

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

from producto import Producto  # Importa la clase Producto del archivo producto.py

class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, marca, modelo):
        """
        Constructor de la clase Electronico.

        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        :param cantidad: Cantidad disponible del producto.
        :param marca: Marca del producto electrónico.
        :param modelo: Modelo del producto electrónico.
        """
        # Llama al constructor de la clase padre Producto para inicializar atributos heredados
        super().__init__(nombre, precio, cantidad)
        # Inicializa el atributo marca del producto electrónico
        self.marca = marca
        # Inicializa el atributo modelo del producto electrónico
        self.modelo = modelo

    def mostrar_informacion(self):
        """
        Muestra la información completa del producto electrónico.
        """
        # Llama al método mostrar_informacion de la clase padre Producto
        super().mostrar_informacion()
        # Imprime la marca del producto electrónico
        print(f"Marca: {self.marca}")
        # Imprime el modelo del producto electrónico
        print(f"Modelo: {self.modelo}")

# Crear instancia de Electronico y mostrar información
if __name__ == "__main__":
    # Crea una instancia de la clase Electronico con valores de ejemplo
    electronico = Electronico("Laptop", 1500.0, 10, "Dell", "XPS 13")
    # Llama al método mostrar_informacion de la instancia creada para mostrar la información
    electronico.mostrar_informacion()