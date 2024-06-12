from producto import Producto

class Electronico(Producto):
    """
    Clase que representa un producto electrónico.
    """

    def __init__(self, nombre, precio, cantidad, marca, modelo):
        """
        Constructor de la clase Electronico.
        
        nombre (str): El nombre del producto.
        precio (float): El precio del producto.
        cantidad (int): La cantidad disponible del producto.
        marca (str): La marca del producto electrónico.
        modelo (str): El modelo del producto electrónico.
        """
        super().__init__(nombre, precio, cantidad)
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        """
        Método que muestra la información específica del producto electrónico.
        """
        super().mostrar_informacion()
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
