class Producto:
    """
    Clase que representa un producto genérico.
    """

    def __init__(self, nombre, precio, cantidad):
        """
        Constructor de la clase Producto.
        nombre (str): El nombre del producto.
        precio (float): El precio del producto.
        cantidad (int): La cantidad disponible del producto.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        """
        Método que muestra la información del producto.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Cantidad disponible: {self.cantidad}")
