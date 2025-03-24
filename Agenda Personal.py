import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime


# Función para agregar un evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if not fecha or not hora or not descripcion:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    try:
        # Verificar si la fecha es válida
        datetime.datetime.strptime(fecha, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Error", "Fecha no válida. Debe ser en formato YYYY-MM-DD.")
        return

    # Agregar el evento a la lista
    eventos_treeview.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar campos
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)


# Función para eliminar un evento seleccionado
def eliminar_evento():
    item = eventos_treeview.selection()
    if not item:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar este evento?")
    if confirmar:
        eventos_treeview.delete(item)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")

# Frame para los eventos
frame_eventos = tk.Frame(ventana)
frame_eventos.pack(padx=10, pady=10)

# Treeview para mostrar los eventos
eventos_treeview = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
eventos_treeview.heading("Fecha", text="Fecha")
eventos_treeview.heading("Hora", text="Hora")
eventos_treeview.heading("Descripción", text="Descripción")
eventos_treeview.pack()

# Frame para agregar un evento
frame_agregar = tk.Frame(ventana)
frame_agregar.pack(padx=10, pady=10)

# Etiquetas y campos de entrada
label_fecha = tk.Label(frame_agregar, text="Fecha (YYYY-MM-DD):")
label_fecha.grid(row=0, column=0, sticky="e")
entry_fecha = tk.Entry(frame_agregar)
entry_fecha.grid(row=0, column=1)

label_hora = tk.Label(frame_agregar, text="Hora (HH:MM):")
label_hora.grid(row=1, column=0, sticky="e")
entry_hora = tk.Entry(frame_agregar)
entry_hora.grid(row=1, column=1)

label_descripcion = tk.Label(frame_agregar, text="Descripción:")
label_descripcion.grid(row=2, column=0, sticky="e")
entry_descripcion = tk.Entry(frame_agregar)
entry_descripcion.grid(row=2, column=1)

# Botones de acción
boton_agregar = tk.Button(frame_agregar, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=3, column=0, columnspan=2, pady=10)

# Botón para eliminar evento
boton_eliminar = tk.Button(ventana, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.pack(padx=10, pady=10)

# Botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()
