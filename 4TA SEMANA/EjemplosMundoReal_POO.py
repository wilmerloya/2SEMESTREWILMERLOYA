# Clase para representar un Vuelo
class Vuelo:
    def __init__(self, numero, origen, destino, asientos_totales, precio):
        """
        Inicializa un vuelo.
        :param numero: Número del vuelo.
        :param origen: Ciudad de origen.
        :param destino: Ciudad de destino.
        :param asientos_totales: Número total de asientos disponibles.
        :param precio: Precio por pasaje.
        """
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.asientos_totales = asientos_totales
        self.asientos_disponibles = asientos_totales
        self.precio = precio

    def reservar_asiento(self):
        """Reserva un asiento si hay disponibilidad."""
        if self.asientos_disponibles > 0:
            self.asientos_disponibles -= 1
            return True
        return False

    def __str__(self):
        """Representación en texto del vuelo."""
        return (f"Vuelo {self.numero}: {self.origen} -> {self.destino} "
                f"Asientos disponibles: {self.asientos_disponibles}/{self.asientos_totales} - "
                f"Precio: ${self.precio:.2f}")


# Clase para representar una Reserva
class Reserva:
    def __init__(self, pasajero, vuelo):
        """
        Inicializa una reserva de pasaje.
        :param pasajero: Nombre del pasajero.
        :param vuelo: Objeto Vuelo reservado.
        """
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.confirmada = False

    def confirmar_reserva(self):
        """Confirma la reserva si hay asientos disponibles en el vuelo."""
        if self.vuelo.reservar_asiento():
            self.confirmada = True
            print(f"Reserva confirmada para {self.pasajero} en el vuelo {self.vuelo.numero}.")
        else:
            print(f"Lo sentimos, no hay asientos disponibles en el vuelo {self.vuelo.numero}.")

    def __str__(self):
        """Representación en texto de la reserva."""
        estado = "Confirmada" if self.confirmada else "Pendiente"
        return f"Reserva de {self.pasajero} en {self.vuelo} - Estado: {estado}"


# Clase para gestionar el sistema de reservas aéreas
class SistemaReservas:
    def __init__(self):
        """Inicializa el sistema con una lista vacía de vuelos."""
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        """Agrega un vuelo al sistema."""
        self.vuelos.append(vuelo)

    def mostrar_vuelos_disponibles(self):
        """Muestra todos los vuelos con asientos disponibles."""
        print("Vuelos disponibles:")
        for vuelo in self.vuelos:
            if vuelo.asientos_disponibles > 0:
                print(vuelo)

    def buscar_vuelo(self, numero):
        """
        Busca un vuelo por número.
        :param numero: Número del vuelo.
        :return: Objeto Vuelo o None si no se encuentra.
        """
        for vuelo in self.vuelos:
            if vuelo.numero == numero:
                return vuelo
        return None


# Código para demostrar el funcionamiento del sistema
if __name__ == "__main__":
    # Crear el sistema de reservas
    sistema = SistemaReservas()

    # Agregar vuelos al sistema
    sistema.agregar_vuelo(Vuelo("Boin 701", "Quito, UIO - Ecuador", "Berlín, BER - Alemania", 100, 723))
    sistema.agregar_vuelo(Vuelo("Boin 411", "Guayaquil, GYE - Ecuador", "París, PAR - Francia", 50, 1015))
    sistema.agregar_vuelo(Vuelo("Boin 802", "Cuenca, CUE - Ecuador", "Barcelona, BCN - España", 200, 1816))

    # Mostrar vuelos disponibles
    sistema.mostrar_vuelos_disponibles()

    # Crear una reserva para un pasajero
    vuelo = sistema.buscar_vuelo("Boin 701")
    if vuelo:
        reserva = Reserva("David Loya", vuelo)
        print(reserva)
        reserva.confirmar_reserva()

    # Intentar reservar un asiento en un vuelo con todos los asientos ocupados
    vuelo_casi_lleno = Vuelo("D404", "París", "Tokio", 1, 1500.00)
    sistema.agregar_vuelo(vuelo_casi_lleno)
    reserva1 = Reserva("María López", vuelo_casi_lleno)
    reserva1.confirmar_reserva()
    reserva2 = Reserva("Carlos Ruiz", vuelo_casi_lleno)
    reserva2.confirmar_reserva()

    # Mostrar vuelos disponibles nuevamente
    sistema.mostrar_vuelos_disponibles()

