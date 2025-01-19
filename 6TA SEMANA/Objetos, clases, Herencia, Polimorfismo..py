# Ejemplo de un programa que demuestra herencia, encapsulación y polimorfismo en Python

# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo público
        self._modelo = modelo  # Atributo protegido

    def detalles(self):
        return f"Marca: {self.marca}, Modelo: {self._modelo}"

# Clase derivada
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.__puertas = puertas  # Atributo privado

    # Método sobrescrito (polimorfismo)
    def detalles(self):
        return f"Marca: {self.marca}, Modelo: {self._modelo}, Puertas: {self.__puertas}"

    # Método para acceder al atributo privado
    def get_puertas(self):
        return self.__puertas

    def set_puertas(self, puertas):
        if puertas > 0:
            self.__puertas = puertas
        else:
            print("El número de puertas debe ser positivo.")

# Clase derivada adicional para demostrar polimorfismo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo  # Atributo público

    # Método sobrescrito (polimorfismo)
    def detalles(self):
        return f"Marca: {self.marca}, Modelo: {self._modelo}, Tipo: {self.tipo}"

# Demostración del programa
if __name__ == "__main__":
    # Crear una instancia de Coche
    mi_coche = Coche("Toyota", "Corolla", 4)
    print(mi_coche.detalles())

    # Modificar y acceder al atributo privado usando métodos
    mi_coche.set_puertas(5)
    print(f"Puertas modificadas: {mi_coche.get_puertas()}")

    # Crear una instancia de Moto
    mi_moto = Moto("Yamaha", "MT-07", "Deportiva")
    print(mi_moto.detalles())

    # Usar polimorfismo
    vehiculos = [mi_coche, mi_moto]
    for vehiculo in vehiculos:
        print(vehiculo.detalles())
