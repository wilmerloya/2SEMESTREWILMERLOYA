import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entry.get()  # Obtener el dato ingresado
    if dato:
        lista_datos.insert(tk.END, dato)  # Agregar el dato a la lista
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un dato.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)  # Limpiar la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Interfaz Gráfica")  # Título de la ventana

# Etiqueta para el campo de texto
etiqueta = tk.Label(ventana, text="Ingresa un dato:")
etiqueta.pack(pady=10)

# Campo de texto para ingresar datos
entry = tk.Entry(ventana, width=30)
entry.pack(pady=5)

# Botón para agregar el dato
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
