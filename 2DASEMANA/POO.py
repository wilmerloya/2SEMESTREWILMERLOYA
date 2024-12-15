# Programa en POO para calcular el promedio semanal del clima

class Clima:
    def __init__(self):
        """
        Constructor de la clase Clima. Inicializa una lista para almacenar las temperaturas semanales.
        """
        self.temperaturas = []

    def agregar_temperaturas(self):
        """
        Solicita al usuario las temperaturas diarias de la semana.
        Almacena las temperaturas en el atributo `temperaturas`.
        """
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        print("Introduce las temperaturas diarias:")
        for dia in dias:
            while True:
                try:
                    temp = float(input(f"Temperatura del {dia}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, introduce un número válido.")

    def calcular_promedio(self):
        """
        Calcula el promedio de las temperaturas almacenadas.
        Retorna el promedio como un número flotante.
        """
        if not self.temperaturas:
            raise ValueError("No se han ingresado temperaturas.")
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_promedio(self):
        """
        Calcula y muestra el promedio semanal al usuario.
        """
        try:
            promedio = self.calcular_promedio()
            print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")
        except ValueError as e:
            print(f"Error: {e}")

# Clase principal para organizar la ejecución
class ProgramaClima:
    def __init__(self):
        """
        Constructor de la clase ProgramaClima. Crea una instancia de Clima.
        """
        self.clima = Clima()

    def ejecutar(self):
        """
        Método principal que coordina la ejecución del programa.
        """
        self.clima.agregar_temperaturas()
        self.clima.mostrar_promedio()

# Punto de entrada principal
if __name__ == "__main__":
    programa = ProgramaClima()
    programa.ejecutar()
