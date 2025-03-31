import tkinter as tk
from tkinter import messagebox

# Función para agregar una tarea
def add_task():
    task = task_entry.get()  # Obtener texto de la entrada
    if task != "":  # Si la tarea no está vacía
        task_listbox.insert(tk.END, task)  # Agregar la tarea a la lista
        task_entry.delete(0, tk.END)  # Limpiar la entrada de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

# Función para marcar la tarea como completada
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()  # Obtener la tarea seleccionada
        task = task_listbox.get(selected_task_index)  # Obtener el texto de la tarea seleccionada
        task_listbox.delete(selected_task_index)  # Eliminar la tarea de la lista
        task_listbox.insert(selected_task_index, task + " (Completada)")  # Volver a agregarla como completada
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcar como completada.")

# Función para eliminar una tarea
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()  # Obtener la tarea seleccionada
        task_listbox.delete(selected_task_index)  # Eliminar la tarea de la lista
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Crear widgets
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Añadir Tarea", width=20, command=add_task)
mark_button = tk.Button(root, text="Marcar como Completada", width=20, command=mark_completed)
delete_button = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)

# Funcionalidad para agregar tarea presionando Enter
root.bind('<Return>', lambda event: add_task())

# Empaquetar los widgets en la ventana
task_entry.pack(pady=10)
add_button.pack(pady=5)
mark_button.pack(pady=5)
delete_button.pack(pady=5)
task_listbox.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
