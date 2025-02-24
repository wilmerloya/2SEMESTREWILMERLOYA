# Ejemplo de clases en Python con constructores (__init__) y destructores (__del__)

class Archivo:
    """Clase para manejar archivos."""

    def __init__(self, nombre):
        """
        Constructor que inicializa el nombre del archivo y abre el archivo en modo escritura.

        :param nombre: Nombre del archivo a crear o escribir.
        """
        self.nombre = nombre
        self.archivo = open(nombre, 'w')  # Abre el archivo en modo escritura
        print(f"Archivo '{self.nombre}' creado y listo para escribir.")

    def escribir(self, texto):
        """
        Escribe texto en el archivo.

        :param texto: Texto a escribir en el archivo.
        """
        self.archivo.write(texto + '\n')  # Escribe una línea de texto en el archivo
        print(f"Texto escrito en '{self.nombre}': {texto}")

    def __del__(self):
        """
        Destructor que cierra el archivo si está abierto y realiza limpieza.
        """
        if self.archivo and not self.archivo.closed:
            self.archivo.close()  # Cierra el archivo
            print(f"Archivo '{self.nombre}' cerrado correctamente.")


# Demostración del uso de constructores y destructores
def main():
    # Crear una instancia de la clase Archivo
    archivo = Archivo("ejemplo.txt")

    # Escribir algunas líneas en el archivo
    archivo.escribir("Hola, este es un ejemplo.")
    archivo.escribir("Usamos __init__ para inicializar.")
    archivo.escribir("El destructor (__del__) cerrará el archivo automáticamente.")

    # Al final de esta función, la variable archivo se elimina y se llama al destructor


if __name__ == "__main__":
    main()
    # Al salir del programa, el destructor será llamado automáticamente.