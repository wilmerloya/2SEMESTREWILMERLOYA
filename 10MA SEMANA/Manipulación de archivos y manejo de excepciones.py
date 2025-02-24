import os
import json


class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga el inventario desde un archivo si existe."""
        if os.path.exists(self.ARCHIVO_INVENTARIO):
            try:
                with open(self.ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
                    self.productos = json.load(archivo)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error al leer el archivo de inventario: {e}")
                self.productos = {}
        else:
            self.guardar_en_archivo()

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo."""
        try:
            with open(self.ARCHIVO_INVENTARIO, "w", encoding="utf-8") as archivo:
                json.dump(self.productos, archivo, indent=4)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo de inventario.")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un producto al inventario y lo guarda en el archivo."""
        if nombre in self.productos:
            print("El producto ya existe. Usa actualizar_producto en su lugar.")
        else:
            self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
            self.guardar_en_archivo()
            print(f"Producto '{nombre}' agregado correctamente.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto existente."""
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre]["cantidad"] = cantidad
            if precio is not None:
                self.productos[nombre]["precio"] = precio
            self.guardar_en_archivo()
            print(f"Producto '{nombre}' actualizado correctamente.")
        else:
            print("Error: El producto no existe en el inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario y lo actualiza en el archivo."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_en_archivo()
            print(f"Producto '{nombre}' eliminado correctamente.")
        else:
            print("Error: El producto no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for nombre, datos in self.productos.items():
                print(f"{nombre} - Cantidad: {datos['cantidad']}, Precio: ${datos['precio']}")


# Ejemplo de uso del sistema
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = input("Nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Nuevo precio (deja en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
