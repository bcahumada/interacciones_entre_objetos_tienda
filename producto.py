"""Módulo que define la clase Producto para representar un producto en la tienda."""

class Producto:
    """Representa un producto con nombre, precio y stock."""

    def __init__(self, nombre, precio, stock=0):
        """Inicializa un nuevo producto.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio del producto.
            stock (int, optional): El stock inicial del producto. Por defecto es 0.
        """
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock if stock >= 0 else 0

    @property
    def nombre(self):
        """Obtiene el nombre del producto.

        Returns:
            str: El nombre del producto.
        """
        return self.__nombre

    @property
    def precio(self):
        """Obtiene el precio del producto.

        Returns:
            float: El precio del producto.
        """
        return self.__precio

    @property
    def stock(self):
        """Obtiene el stock actual del producto.

        Returns:
            int: El stock del producto.
        """
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        """Establece un nuevo valor para el stock del producto.

        Args:
            nuevo_stock (int): El nuevo stock del producto. Debe ser mayor o igual a 0.
        """
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            self.__stock = 0

    def __add__(self, other):
        """Permite sumar el stock de dos productos si tienen el mismo nombre.

        Args:
            other (Producto): El otro producto con el que se suma el stock.

        Returns:
            Producto: Un nuevo objeto Producto con el stock sumado.

        Raises:
            ValueError: Si los productos tienen nombres diferentes.
        """
        if self.__nombre == other.__nombre:
            return Producto(self.__nombre, self.__precio, self.__stock + other.__stock)
        else:
            raise ValueError("No se pueden sumar productos distintos.")

    def __sub__(self, cantidad):
        """Permite restar una cantidad del stock del producto.

        Args:
            cantidad (int): La cantidad a restar del stock.

        Returns:
            Producto: Un nuevo objeto Producto con el stock actualizado.
        """
        if self.__stock >= cantidad:
            return Producto(self.__nombre, self.__precio, self.__stock - cantidad)
        else:
            return Producto(self.__nombre, self.__precio, 0)

    def __eq__(self, other):
        """Compara dos productos por su nombre.

        Args:
            other (Producto): El otro producto con el que se compara.

        Returns:
            bool: True si los nombres de los productos son iguales, False en caso contrario.
        """
        return self.__nombre == other.__nombre