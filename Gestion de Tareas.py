import tkinter as tk
from tkinter import messagebox

# Funciones para manejar las tareas
def añadir_tarea():
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

def marcar_como_completada():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]  # Obtener la tarea seleccionada
        tarea = lista_tareas.get(tarea_seleccionada)
        # Marcar la tarea como completada añadiendo un "✔"
        tarea_completada = "✔ " + tarea
        lista_tareas.delete(tarea_seleccionada)  # Eliminar la tarea original
        lista_tareas.insert(tarea_seleccionada, tarea_completada)  # Insertar la tarea marcada como completada
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")

def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]  # Obtener la tarea seleccionada
        lista_tareas.delete(tarea_seleccionada)  # Eliminar la tarea seleccionada
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")

def cerrar_app(event=None):
    root.quit()  # Cerrar la aplicación

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas Pendientes")

# Crear los widgets
entrada_tarea = tk.Entry(root, width=50)
boton_añadir = tk.Button(root, text="Añadir tarea", command=añadir_tarea)
boton_completar = tk.Button(root, text="Marcar como completada", command=marcar_como_completada)
boton_eliminar = tk.Button(root, text="Eliminar tarea", command=eliminar_tarea)
lista_tareas = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)

# Colocar los widgets en la ventana
entrada_tarea.pack(pady=10)
boton_añadir.pack(pady=5)
boton_completar.pack(pady=5)
boton_eliminar.pack(pady=5)
lista_tareas.pack(pady=10)

# Configurar atajos de teclado
root.bind("<Return>", lambda event: añadir_tarea())  # Tecla Enter para añadir tarea
root.bind("<c>", lambda event: marcar_como_completada())  # Tecla C para marcar como completada
root.bind("<Delete>", lambda event: eliminar_tarea())  # Tecla Delete para eliminar tarea
root.bind("<d>", lambda event: eliminar_tarea())  # Tecla D para eliminar tarea
root.bind("<Escape>", cerrar_app)  # Tecla Escape para cerrar la aplicación

# Iniciar el bucle de eventos
root.mainloop()
