# Programa para gestionar un registro básico de entrenamiento físico.
# Funcionalidad: Permite agregar registros de entrenamiento, mostrar todos los registros y calcular el promedio de calorías quemadas.
# Utiliza diferentes tipos de datos: integer, float, string y boolean.

# Lista para almacenar los registros de entrenamiento
registro_entrenamiento = []


def agregar_entrenamiento(nombre_participante, duracion_minutos, calorias_quemadas, completado):
    """
    Agrega un registro de entrenamiento al sistema.

    :param nombre_participante: Nombre del participante (string)
    :param duracion_minutos: Duración del entrenamiento en minutos (integer)
    :param calorias_quemadas: Calorías quemadas durante el entrenamiento (float)
    :param completado: Indica si el entrenamiento fue completado (boolean)
    """
    entrenamiento = {
        "nombre_participante": nombre_participante,
        "duracion_minutos": duracion_minutos,
        "calorias_quemadas": calorias_quemadas,
        "completado": completado
    }
    registro_entrenamiento.append(entrenamiento)
    print(f"Registro de entrenamiento para {nombre_participante} agregado correctamente.")


def mostrar_registros():
    """Muestra todos los registros de entrenamiento almacenados."""
    if not registro_entrenamiento:
        print("No hay registros de entrenamiento disponibles.")
        return
    print("Registros de Entrenamiento:")
    for i, entrenamiento in enumerate(registro_entrenamiento, start=1):
        estado = "Completado" if entrenamiento["completado"] else "No completado"
        print(
            f"{i}. Nombre: {entrenamiento['nombre_participante']}, Duración: {entrenamiento['duracion_minutos']} min, "
            f"Calorías: {entrenamiento['calorias_quemadas']} cal, Estado: {estado}")


def calcular_promedio_calorias():
    """Calcula y muestra el promedio de calorías quemadas."""
    if not registro_entrenamiento:
        print("No hay registros para calcular el promedio de calorías quemadas.")
        return
    total_calorias = sum(entrenamiento["calorias_quemadas"] for entrenamiento in registro_entrenamiento)
    promedio = total_calorias / len(registro_entrenamiento)
    print(f"El promedio de calorías quemadas es: {promedio:.2f} cal.")


# Ejecución del programa
# Agregar algunos registros de entrenamiento
agregar_entrenamiento("David Loya", 52, 150, True)
agregar_entrenamiento("Juan Andrade", 32, 100.0, True)
agregar_entrenamiento("Paola Vite", 60, 400.7, False)

# Mostrar los registros de entrenamiento
mostrar_registros()

# Calcular el promedio de calorías quemadas
calcular_promedio_calorias()
