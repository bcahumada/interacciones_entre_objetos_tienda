"""Módulo principal para gestionar las tiendas y las ventas."""

from tienda import Restaurante, Supermercado, Farmacia, Producto

tiendas = []  # Lista para almacenar las tiendas creadas


def crear_tienda():
    """Crea una nueva tienda."""
    while True:
        tipo_tienda = input(
            "\nIngrese el tipo de tienda \n1: Restaurante \n2: Supermercado \n3: Farmacia \nTipo de tienda: "
        )
        if tipo_tienda in ["1", "2", "3"]:
            break
        else:
            print("\nTipo de tienda inválido. Ingrese 1, 2 o 3.")

    nombre = input("\nIngrese el nombre de la tienda: ")
    while not nombre:  # Validar que el nombre no esté vacío
        print("\nDebes asignarle un nombre a la tienda.")
        nombre = input("Ingrese el nombre de la tienda: ")

    while True:
        costo_delivery_str = input("Ingrese el costo de delivery: ")
        try:
            costo_delivery = float(costo_delivery_str)
            if costo_delivery >= 0:
                break
            else:
                print("\nEl costo de delivery no puede ser negativo.")
        except ValueError:
            print("\nIngreso inválido. Debe ingresar un número para el costo de delivery.")

    if tipo_tienda == "1":
        tienda = Restaurante(nombre, costo_delivery)
    elif tipo_tienda == "2":
        tienda = Supermercado(nombre, costo_delivery)
    elif tipo_tienda == "3":
        tienda = Farmacia(nombre, costo_delivery)

    tiendas.append(tienda)
    return tienda


def administrar_tienda(tienda):
    """Administra las operaciones de una tienda específica."""
    while True:
        print("\nOpciones:")
        print("1. Listar productos")
        print("2. Realizar venta")
        print("3. Agregar producto")
        print("4. Volver al Inicio")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mensaje_productos = tienda.listar_productos()
            if mensaje_productos.startswith("No se han ingresado"):
                if isinstance(tienda, Restaurante):
                    mensaje_productos = f"\nNo se han ingresado platos en el restaurante \"{tienda.nombre}\" aún."
                else:
                    mensaje_productos = (
                        f"No se han ingresado productos en \"{tienda.nombre}\" aún."
                    )
            print(mensaje_productos)

        elif opcion == "2":
            # ¡Usar la MISMA verificación que en la opción "1. Listar productos"!
            mensaje_productos = tienda.listar_productos()
            if mensaje_productos.startswith("No se han ingresado"):
                print(mensaje_productos)  # Mostrar el mensaje de que no hay productos
            else:  # Si hay productos, procede con la venta
                total_venta = 0
                costo_delivery_aplicado = tienda.costo_delivery
                productos_a_vender = []

                while True:
                    nombre_producto = input(
                        "Ingrese el nombre del producto a vender (o 'fin' para finalizar): "
                    )
                    if nombre_producto.lower() == "fin":
                        break

                    while True:
                        cantidad_str = input("Ingrese la cantidad: ")
                        try:
                            cantidad = int(cantidad_str)
                            if cantidad > 0:
                                # Validar stock al ingresar la cantidad (excepto para restaurantes)
                                if not isinstance(tienda, Restaurante):
                                    for p in tienda._Tienda__productos:
                                        if (
                                            p.nombre == nombre_producto
                                            and p.stock < cantidad
                                        ):
                                            print(
                                                f"Alerta: Stock insuficiente de {nombre_producto}. Solo quedan {p.stock} unidades disponibles.\n Se venderán las unidades disponibles."
                                            )
                                            cantidad = (
                                                p.stock
                                            )  # Actualizar cantidad a la disponible
                                            break  # Salir del bucle de búsqueda de producto

                                # Validar máximo 3 unidades en farmacias
                                if isinstance(tienda, Farmacia) and cantidad > 3:
                                    print(
                                        "\nSolo puedes vender un máximo de 3 unidades por producto. Ingresa la cantidad nuevamente."
                                    )
                                else:
                                    break  # Salir del bucle de cantidad si la cantidad es válida
                            else:
                                print(
                                    "La cantidad debe ser mayor que cero. Intente de nuevo."
                                )
                        except ValueError:
                            print(
                                "Ingreso inválido. Debe ingresar un número para la cantidad."
                            )

                    productos_a_vender.append((nombre_producto, cantidad))

                # Verificar si se agregaron productos a la venta
                if productos_a_vender:  # Si la lista no está vacía
                    print("\n--- Detalles de la venta ---")
                    for nombre_producto, cantidad in productos_a_vender:
                        (
                            exito,
                            subtotal,
                            cantidad_vendida,
                        ) = tienda.realizar_venta(
                            nombre_producto, cantidad
                        )
                        if exito:
                            for producto in tienda._Tienda__productos:
                                if producto.nombre == nombre_producto:
                                    precio_unitario = producto.precio
                                    break
                            print(
                                f"{nombre_producto} - ${precio_unitario} x {cantidad_vendida} unidades - Subtotal: ${subtotal:.2f}"
                            )
                            total_venta += subtotal
                            # Aplicar descuento de delivery solo si no se ha aplicado antes
                            if (
                                isinstance(tienda, Farmacia)
                                and total_venta > 15000
                                and costo_delivery_aplicado != 0  # Verificar si el costo de delivery ya se ha aplicado
                            ):
                                costo_delivery_aplicado = 0
                        else:
                            print(
                                f"El producto '{nombre_producto}' no existe en el inventario."
                            )

                    print(f"Costo de Delivery: ${costo_delivery_aplicado:.2f}")
                    print(
                        f"Total de la venta: ${total_venta + costo_delivery_aplicado:.2f}"
                    )

                    if (
                        isinstance(tienda, Farmacia)
                        and total_venta > 15000
                        and costo_delivery_aplicado == 0
                    ):
                        print(
                            "\n¡Entrega gratis por compras sobre $15.000 en productos de farmacia!"
                        )
                else:
                    print("\nNo se ha realizado ninguna venta.")

        elif opcion == "3":
            while True:
                nombre_producto = input("\nIngrese el nombre del producto: ")
                while not nombre_producto:  # Validar que el nombre no esté vacío
                    print("\nEl producto debe tener un nombre.")
                    nombre_producto = input("Ingrese el nombre del producto: ")

                while True:
                    precio_producto_str = input("Ingrese el precio del producto: ")
                    try:
                        precio_producto = float(precio_producto_str)
                        if precio_producto >= 0:
                            break
                        else:
                            print("\nEl precio del producto no puede ser negativo.")
                    except ValueError:
                        print(
                            "\nIngreso inválido. Debe ingresar un número para el precio del producto."
                        )

                if isinstance(tienda, Restaurante):
                    stock_producto = 0
                else:
                    while True:
                        stock_producto_str = input(
                            "Ingrese el stock del producto (dejar en blanco si no hay stock): "
                        )
                        if not stock_producto_str:
                            stock_producto = 0
                            break
                        try:
                            stock_producto = int(stock_producto_str)
                            if stock_producto >= 0:
                                break
                            else:
                                print("\nEl stock no puede ser negativo.")
                        except ValueError:
                            print(
                                "\nIngreso inválido. Debe ingresar un número para el stock."
                            )

                producto = Producto(
                    nombre_producto, precio_producto, stock_producto
                )
                tienda.ingresar_producto(producto)
                print(f"\nProducto '{nombre_producto}' agregado correctamente.")

                agregar_otro = input("¿Desea agregar otro producto? (s/n): ")
                if agregar_otro.lower() != "s":
                    break
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


def main():
    """Función principal del programa."""
    while True:
        print("\nBienvenido! Has ingresado al sistema")
        print("\n1. Crear una nueva tienda")
        print("2. Administrar una tienda existente")
        print("3. Salir")
        opcion = input("\nSeleccione una opción del menú: ")

        if opcion == "1":
            tienda = crear_tienda()
            if tienda:
                administrar_tienda(tienda)
        elif opcion == "2":
            if tiendas:
                print("\nTiendas existentes:")
                for i, t in enumerate(tiendas):
                    print(f"{i+1}. {t.nombre}")
                print(f"{len(tiendas) + 1}. Volver al inicio") # Opción para volver al inicio

                while True:
                    opcion_tienda = input(
                        f"Seleccione una tienda (1-{len(tiendas) + 1}): " # Ajustar el rango de opciones
                    )
                    try:
                        indice_tienda = int(opcion_tienda) - 1
                        if 0 <= indice_tienda < len(tiendas):
                            tienda = tiendas[indice_tienda]
                            administrar_tienda(tienda)
                            break
                        elif indice_tienda == len(tiendas): # Opción para volver al inicio
                            break  # Salir del bucle de selección de tienda
                        else:
                            print("\nOpción de tienda inválida.")
                    except ValueError:
                        print("\nIngresa un número válido para seleccionar la tienda.")
            else:
                print("\nNo hay tiendas creadas. Debes crear una primero.")
        elif opcion == "3":
            print("Hasta pronto!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()