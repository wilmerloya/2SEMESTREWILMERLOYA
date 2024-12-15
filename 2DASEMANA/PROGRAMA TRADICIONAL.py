# Programa en programación tradicional para calcular el promedio semanal del clima

def obtener_temperaturas():
    """
    Solicita al usuario las temperaturas diarias de la semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    print("Introduce las temperaturas diarias:")
    for dia in dias:
        while True:
            try:
                temp = float(input(f"Temperatura del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, introduce un número válido.")
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Retorna el promedio como un número flotante.
    """
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultado(promedio):
    """
    Muestra el resultado del promedio semanal al usuario.
    """
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Flujo principal del programa
def main():
    temperaturas = obtener_temperaturas()
    promedio = calcular_promedio(temperaturas)
    mostrar_resultado(promedio)

# Ejecutar el programa
if __name__ == "__main__":
    main()
