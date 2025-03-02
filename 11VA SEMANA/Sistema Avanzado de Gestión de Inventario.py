class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.producto_id

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    import pickle

    class Inventario:
        def __init__(self):
            self.productos = {}  # Diccionario para almacenar productos, donde el ID es la clave

        def añadir_producto(self, producto):
            if producto.obtener_id() in self.productos:
                print("El producto ya existe en el inventario.")
            else:
                self.productos[producto.obtener_id()] = producto
                print(f"Producto {producto.obtener_nombre()} añadido con éxito.")

        def eliminar_producto(self, producto_id):
            if producto_id in self.productos:
                del self.productos[producto_id]
                print(f"Producto con ID {producto_id} eliminado con éxito.")
            else:
                print(f"No se encontró un producto con ID {producto_id}.")

        def actualizar_producto(self, producto_id, cantidad=None, precio=None):
            if producto_id in self.productos:
                producto = self.productos[producto_id]
                if cantidad is not None:
                    producto.actualizar_cantidad(cantidad)
                if precio is not None:
                    producto.actualizar_precio(precio)
                print(f"Producto con ID {producto_id} actualizado con éxito.")
            else:
                print(f"No se encontró un producto con ID {producto_id}.")

        def buscar_producto(self, nombre):
            encontrados = [producto for producto in self.productos.values() if
                           nombre.lower() in producto.obtener_nombre().lower()]
            if encontrados:
                for producto in encontrados:
                    print(producto)
            else:
                print(f"No se encontraron productos con el nombre '{nombre}'.")

        def mostrar_inventario(self):
            if not self.productos:
                print("El inventario está vacío.")
            else:
                for producto in self.productos.values():
                    print(producto)

        def guardar_inventario(self, archivo="inventario.pkl"):
            with open(archivo, "wb") as f:
                import pickle
                pickle.dump(self.productos, f)
            print("Inventario guardado con éxito.")

        def cargar_inventario(self, archivo="inventario.pkl"):
            try:
                with open(archivo, "rb") as f:
                    self.productos = pickle.load(f)
                print("Inventario cargado con éxito.")
            except FileNotFoundError:
                print("No se encontró el archivo de inventario.")


def mostrar_menu():
    print("\n-- Sistema de Gestión de Inventario --")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto")
    print("5. Mostrar Inventario")
    print("6. Guardar Inventario")
    print("7. Cargar Inventario")
    print("8. Salir")


def Inventario():
    pass


def interfaz_usuario():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            producto_id = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(producto_id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            producto_id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(producto_id)

        elif opcion == "3":
            producto_id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (deja vacío si no deseas cambiarla): ")
            precio = input("Nuevo precio (deja vacío si no deseas cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(producto_id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            inventario.guardar_inventario()

        elif opcion == "7":
            inventario.cargar_inventario()

        elif opcion == "8":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, selecciona nuevamente.")

if __name__ == "__main__":
    interfaz_usuario()
