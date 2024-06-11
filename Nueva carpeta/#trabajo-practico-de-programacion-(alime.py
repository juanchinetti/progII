#trabajo-practico-de-programacion-(alimentos)

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

from producto import Producto  #Importa la clase Producto del archivo producto.py

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        """
        Constructor de la clase Alimento.

         nombre: Nombre del producto.
         precio: Precio del producto.
         cantidad: Cantidad disponible del producto.
         fecha_expiracion: Fecha de expiración del producto alimenticio.
        """
        #Llama al constructor de la clase padre Producto para inicializar atributos heredados
        super().__init__(nombre, precio, cantidad)
        #Inicializa el atributo fecha de expiración del producto alimenticio
        self.fecha_expiracion = fecha_expiracion

    def mostrar_informacion(self):
        """
        Muestra la información completa del producto alimenticio.
        """
        #Llama al método mostrar_informacion de la clase padre Producto
        super().mostrar_informacion()
        #Imprime la fecha de expiración del producto alimenticio
        print(f"Fecha de Expiración: {self.fecha_expiracion}")

#Crear instancia de Alimento y mostrar información
if __name__ == "__main__":
    #Crea una instancia de la clase Alimento con valores de ejemplo
    alimento = Alimento("naranja", 0.5, 100, "2024-08-29")
    #Llama al método mostrar_informacion de la instancia creada para mostrar la información
    alimento.mostrar_informacion()
