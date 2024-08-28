## Sistema de Ventas con Python
Este proyecto implementa un sistema de ventas simple utilizando Python y el paradigma orientado a objetos. Permite crear diferentes tipos de tiendas (restaurantes, supermercados y farmacias), agregar productos, listar productos disponibles y realizar ventas con detalles y cálculo de costos, incluyendo el delivery.

### Características principales
Gestión de tiendas: Permite crear y administrar diferentes tipos de tiendas:
Restaurante: Los platos no tienen stock, ya que se preparan al momento de la venta.
Supermercado: Se gestiona el stock de productos, con avisos si hay "pocos productos disponibles".
Farmacia: Se gestiona el stock con un límite de 3 unidades por venta y se ofrece envío gratis en compras superiores a $15.000.
Gestión de productos: Permite agregar productos, actualizar el stock y listar los productos disponibles en cada tienda.
Realizar ventas: Se pueden realizar ventas de uno o varios productos, con un detalle que incluye:
Nombre del producto
Precio unitario
Cantidad de unidades
Subtotal
Costo de delivery
Total de la venta
Mensajes informativos: El sistema proporciona mensajes claros al usuario en diferentes situaciones, como:
Stock insuficiente
Producto no encontrado
Superación del límite de unidades a vender en farmacias
Almacenamiento de datos: Las tiendas creadas y sus productos se almacenan en memoria durante la ejecución del programa.

### Cómo ejecutar el programa
#### Requisitos
Python 3.x 
Descarga los archivos tienda.py , producto.py y programa.py.
Ejecuta el archivo programa.py desde la terminal: python programa.py

Sigue las instrucciones del menú para crear tiendas, agregar productos y realizar ventas.

### Estructura del proyecto
tienda.py: Contiene las clases que representan los diferentes tipos de tiendas (Tienda, Restaurante, Supermercado, Farmacia) y la lógica para gestionar productos y ventas.
programa.py: Contiene el código principal del programa, incluyendo el menú interactivo y la lógica para crear y administrar tiendas.
producto.py: Contiene la clase Producto que representa un producto con nombre, precio y stock.



### Autor

Bárbara HA

Github: https://github.com/bcahumada/