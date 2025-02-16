class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y Setters
    def get_id(self):
        return self.id_producto

    def set_id(self, id_producto):
        self.id_producto = id_producto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    # Añadir producto
    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        # Verificar si el ID ya existe
        for producto in self.productos:
            if producto.get_id() == id_producto:
                print(f"Error: Ya existe un producto con ID {id_producto}.")
                return
        # Si el ID es único, agregar el producto
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print(f"Producto {nombre} agregado con éxito.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                print(f"Producto con ID {id_producto} eliminado.")
                return
        print(f"Error: Producto con ID {id_producto} no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print(f"Producto con ID {id_producto} actualizado.")
                return
        print(f"Error: Producto con ID {id_producto} no encontrado.")

    # Buscar productos por nombre
    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            print(f"Productos encontrados con el nombre '{nombre}':")
            for producto in encontrados:
                print(
                    f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    # Mostrar todos los productos
    def mostrar_todos_productos(self):
        if self.productos:
            print("Productos en el inventario:")
            for producto in self.productos:
                print(
                    f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
        else:
            print("El inventario está vacío.")


# Interfaz de Usuario en la Consola
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Todos los Productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            inventario.agregar_producto(id_producto, nombre, cantidad, precio)

        elif opcion == '2':
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje en blanco para no actualizar): ")
            precio = input("Ingrese nuevo precio (deje en blanco para no actualizar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_todos_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()
