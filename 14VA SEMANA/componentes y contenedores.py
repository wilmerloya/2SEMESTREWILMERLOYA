import tkinter as tk
from tkinter import ttk, messagebox


def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos")


def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        tree.delete(seleccionado)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")


# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Etiquetas y campos de entrada
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

label_fecha = tk.Label(frame_entrada, text="Fecha (DD/MM/AAAA):")
label_fecha.grid(row=0, column=0, padx=5, pady=5)
entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

label_hora = tk.Label(frame_entrada, text="Hora (HH:MM):")
label_hora.grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5, pady=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=2, padx=5, pady=5)

# Lista de eventos (TreeView)
columns = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
