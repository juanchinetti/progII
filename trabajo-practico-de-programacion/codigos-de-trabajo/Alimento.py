from producto import Producto

class Alimento(Producto):
    """
    Clase que representa un producto alimenticio.
    """

    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        """
        Constructor de la clase Alimento.

        Args:
        nombre (str): El nombre del producto.
        precio (float): El precio del producto.
        cantidad (int): La cantidad disponible del producto.
        fecha_expiracion (str): La fecha de expiración del producto alimenticio.
        """
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

    def mostrar_informacion(self):
        """
        Método que muestra la información específica del producto alimenticio.
        """
        super().mostrar_informacion()
        print(f"Fecha de expiración: {self.fecha_expiracion}")