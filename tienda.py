"""Módulo que contiene las clases para gestionar diferentes tipos de tiendas y productos."""

from producto import Producto


class Tienda:
    """Clase base para representar una tienda."""

    def __init__(self, nombre, costo_delivery):
        """Inicializa una nueva tienda con su nombre y costo de delivery.

        Args:
            nombre (str): El nombre de la tienda.
            costo_delivery (float): El costo de delivery de la tienda.
        """
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        """Obtiene el nombre de la tienda.

        Returns:
            str: El nombre de la tienda.
        """
        return self.__nombre

    @property
    def costo_delivery(self):
        """Obtiene el costo de delivery de la tienda.

        Returns:
            float: El costo de delivery de la tienda.
        """
        return self.__costo_delivery

    def ingresar_producto(self, producto):
        """Ingresa un nuevo producto a la tienda o actualiza su stock si ya existe.

        Args:
            producto (Producto): El producto a ingresar.
        """
        for p in self.__productos:
            if p == producto:
                p.stock += producto.stock
                return
        self.__productos.append(producto)

    def listar_productos(self):
        """Lista los productos disponibles en la tienda.

        Returns:
            str: Una cadena con la lista de productos formateada, o un mensaje si no hay productos.
        """
        if self.__productos:
            return "Productos en la tienda {}:\n{}".format(
                self.nombre, "\n".join(str(p) for p in self.__productos)
            )
        else:
            return f"\nNo se han ingresado productos en esta {self.nombre} aún."

    def realizar_venta(self, nombre_producto, cantidad):
        """Realiza una venta de un producto específico.

        Args:
            nombre_producto (str): El nombre del producto a vender.
            cantidad (int): La cantidad de unidades a vender.

        Returns:
            tuple: Una tupla (bool, float, int) que indica si la venta fue exitosa, el subtotal, y la cantidad vendida
                   o (False, 0, 0) si no se encontró el producto.
        """
        for p in self.__productos:
            if p.nombre == nombre_producto:
                if p.stock >= cantidad:  # Hay suficiente stock
                    p.stock -= cantidad
                    return True, p.precio * cantidad, cantidad
                else:  # No hay suficiente stock, vender lo disponible
                    cantidad_vendida = p.stock
                    p.stock = 0  # Actualizar el stock a cero
                    return True, p.precio * cantidad_vendida, cantidad_vendida
        return False, 0, 0  # No se encontró el producto


class Restaurante(Tienda):
    """Clase para representar un restaurante, hereda de Tienda."""

    def __init__(self, nombre, costo_delivery):
        """Inicializa un nuevo restaurante."""
        super().__init__(nombre, costo_delivery)

    def ingresar_producto(self, producto):
        """Ingresa un nuevo plato al restaurante (el stock siempre será 0)."""
        producto.stock = 0
        super().ingresar_producto(producto)

    def listar_productos(self):
        """Lista los platos disponibles en el restaurante.

        Returns:
            str: Una cadena con la lista de platos formateada, o un mensaje si no hay platos.
        """
        if self._Tienda__productos:
            return "Platos en el restaurante {}:\n{}".format(
                self.nombre,
                "\n".join(f"{p.nombre} - ${p.precio}" for p in self._Tienda__productos),
            )
        else:
            return f"No se han ingresado platos en este restaurante aún."

    def realizar_venta(self, nombre_producto, cantidad):
        """Realiza una venta de un plato (no se gestiona el stock en restaurantes).

        Returns:
            tuple: Una tupla (bool, float, int) que indica si la venta fue exitosa, el subtotal, y la cantidad vendida
                   o (False, 0, 0) si no se encontró el plato.
        """
        for p in self._Tienda__productos:
            if p.nombre == nombre_producto:
                return True, p.precio * cantidad, cantidad # Retorna la cantidad vendida
        return False, 0, 0  # No se encontró el plato


class Supermercado(Tienda):
    """Clase para representar un supermercado, hereda de Tienda."""

    def __init__(self, nombre, costo_delivery):
        """Inicializa un nuevo supermercado."""
        super().__init__(nombre, costo_delivery)

    def listar_productos(self):
        """Lista los productos disponibles en el supermercado.

        Returns:
            str: Una cadena con la lista de productos formateada, o un mensaje si no hay productos.
        """
        if self._Tienda__productos:
            productos_formateados = []
            for p in self._Tienda__productos:
                mensaje_stock = (
                    " (Pocos productos disponibles)" if p.stock < 10 else ""
                )
                productos_formateados.append(
                    f"{p.nombre} - ${p.precio} ({p.stock} unidades disponibles{mensaje_stock})"
                )
            return "Productos en el supermercado {}:\n{}".format(
                self.nombre, "\n".join(productos_formateados)
            )
        else:
            return f"No se han ingresado productos en este supermercado aún."


class Farmacia(Tienda):
    """Clase para representar una farmacia, hereda de Tienda."""

    def __init__(self, nombre, costo_delivery):
        """Inicializa una nueva farmacia."""
        super().__init__(nombre, costo_delivery)

    def listar_productos(self):
        """Lista los productos disponibles en la farmacia.

        Returns:
            str: Una cadena con la lista de productos formateada, o un mensaje si no hay productos.
        """
        if self._Tienda__productos:
            productos_formateados = []
            for p in self._Tienda__productos:
                mensaje_envio = (
                    " (Envío gratis al solicitar este producto)"
                    if p.precio > 15000
                    else ""
                )
                productos_formateados.append(
                    f"{p.nombre} - ${p.precio}{mensaje_envio}"
                )
            return "Productos en la farmacia {}:\n{}".format(
                self.nombre, "\n".join(productos_formateados)
            )
        else:
            return f"No se han ingresado productos en esta farmacia aún."

    def realizar_venta(self, nombre_producto, cantidad):
        """Realiza una venta de un producto, con un límite de 3 unidades por producto.

        Args:
            nombre_producto (str): El nombre del producto a vender.
            cantidad (int): La cantidad de unidades a vender.

        Returns:
            tuple: Una tupla (bool, float, int) que indica si la venta fue exitosa, el subtotal, y la cantidad vendida
                   o (False, 0, 0) si no se encontró el producto.
        """
        for p in self._Tienda__productos:
            if p.nombre == nombre_producto:
                if cantidad > 3:
                    print(
                        f"Alerta: No se pueden vender más de 3 unidades de {nombre_producto}. Se venderán 3 unidades."
                    )
                    cantidad = 3
                if p.stock >= cantidad:
                    p.stock -= cantidad
                    return True, p.precio * cantidad, cantidad  # Devolver cantidad también
                else:
                    print(
                        f"Alerta: Stock insuficiente de {nombre_producto}. Se venderá la cantidad disponible: {p.stock}"
                    )
                    cantidad_disponible = p.stock
                    p.stock = 0
                    return (
                        True,
                        p.precio * cantidad_disponible,
                        cantidad_disponible,
                    )  # Devolver cantidad_disponible
        return False, 0, 0  # No se encontró el producto