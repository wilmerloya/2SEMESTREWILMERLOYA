# Clase base (Padre)
class Vehiculo:
    def __init__(self, marca, modelo, anio, color):
        # Atributos encapsulados con '_'
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._color = color
        self._encendido = False  # Atributo para verificar si el vehículo está encendido

    # Método de abstracción: muestra información general del vehículo
    def mostrar_informacion(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    # Método para encender el vehículo
    def encender(self):
        if not self._encendido:
            self._encendido = True
            print(f"{self._marca} {self._modelo} ha sido encendido.")
        else:
            print(f"{self._marca} {self._modelo} ya está encendido.")

    # Método para apagar el vehículo
    def apagar(self):
        if self._encendido:
            self._encendido = False
            print(f"{self._marca} {self._modelo} ha sido apagado.")
        else:
            print(f"{self._marca} {self._modelo} ya está apagado.")

    # Método para obtener información general del vehículo
    def obtener_info(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._anio}, Color: {self._color}"

# Clase derivada (Hija) - Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, color, puertas):
        # Llamada al constructor de la clase base (padre)
        super().__init__(marca, modelo, anio, color)
        self._puertas = puertas  # Atributo adicional específico para Coche

    # Implementación del método abstracto
    def mostrar_informacion(self):
        return f"{self.obtener_info()}, Puertas: {self._puertas}"

    # Método específico de Coche
    def tocar_bocina(self):
        print(f"{self._marca} {self._modelo} está tocando la bocina: ¡BEEP BEEP!")

# Clase derivada (Hija) - Camion
class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, color, carga_maxima):
        # Llamada al constructor de la clase base (padre)
        super().__init__(marca, modelo, anio, color)
        self._carga_maxima = carga_maxima  # Atributo adicional específico para Camion

    # Implementación del método abstracto
    def mostrar_informacion(self):
        return f"{self.obtener_info()}, Carga máxima: {self._carga_maxima}kg"

    # Método específico de Camion
    def cargar(self, peso):
        if peso <= self._carga_maxima:
            print(f"{self._marca} {self._modelo} está cargando {peso}kg.")
        else:
            print(f"Error: No puedes cargar más de {self._carga_maxima}kg en este camión.")

# Clase derivada (Hija) - Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, color, tipo):
        super().__init__(marca, modelo, anio, color)
        self._tipo = tipo  # Atributo adicional específico para Motocicleta

    # Implementación del método abstracto
    def mostrar_informacion(self):
        return f"{self.obtener_info()}, Tipo: {self._tipo}"

    # Método específico de Motocicleta
    def hacer_caballito(self):
        print(f"{self._marca} {self._modelo} está haciendo un caballito. ¡Wooow!")

# Uso de las clases

# Crear instancias de cada clase
coche = Coche("Toyota", "Corolla", 2020, "Rojo", 4)
camion = Camion("Volvo", "FH16", 2022, "Azul", 20000)
motocicleta = Motocicleta("Harley-Davidson", "Street 750", 2023, "Negro", "Cruiser")

# Mostrar información de cada vehículo
print(coche.mostrar_informacion())
print(camion.mostrar_informacion())
print(motocicleta.mostrar_informacion())

# Encender y apagar los vehículos
coche.encender()
camion.encender()
motocicleta.encender()

# Realizar acciones específicas
coche.tocar_bocina()
camion.cargar(15000)
motocicleta.hacer_caballito()

# Apagar los vehículos
coche.apagar()
camion.apagar()
motocicleta.apagar()
