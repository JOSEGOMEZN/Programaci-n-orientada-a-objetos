import tkinter as tk
from tkinter import messagebox

# Función para agregar la información a la lista
def agregar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    ciudad = entry_ciudad.get()
    tipo_sangre = entry_tipo_sangre.get()
    genero = entry_genero.get()
    alergias = entry_alergias.get()

    # Validación simple: verificar si hay algún campo vacío
    if not nombre or not edad or not ciudad or not tipo_sangre or not genero or not alergias:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return

    # Agregar los datos a la lista
    lista_datos.insert(tk.END, f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}, Tipo de Sangre: {tipo_sangre}, Género: {genero}, Alergias: {alergias}")

    # Limpiar los campos de texto
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_ciudad.delete(0, tk.END)
    entry_tipo_sangre.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_alergias.delete(0, tk.END)

# Función para limpiar todos los campos de texto
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_ciudad.delete(0, tk.END)
    entry_tipo_sangre.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_alergias.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Datos Personales")

# Crear las etiquetas
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=10)

label_edad = tk.Label(ventana, text="Edad:")
label_edad.grid(row=1, column=0, padx=10, pady=10)

label_ciudad = tk.Label(ventana, text="Ciudad:")
label_ciudad.grid(row=2, column=0, padx=10, pady=10)

label_tipo_sangre = tk.Label(ventana, text="Tipo de Sangre:")
label_tipo_sangre.grid(row=3, column=0, padx=10, pady=10)

label_genero = tk.Label(ventana, text="Género:")
label_genero.grid(row=4, column=0, padx=10, pady=10)

label_alergias = tk.Label(ventana, text="Alergias:")
label_alergias.grid(row=5, column=0, padx=10, pady=10)

# Crear los campos de texto para ingresar los datos
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1, padx=10, pady=10)

entry_ciudad = tk.Entry(ventana)
entry_ciudad.grid(row=2, column=1, padx=10, pady=10)

entry_tipo_sangre = tk.Entry(ventana)
entry_tipo_sangre.grid(row=3, column=1, padx=10, pady=10)

entry_genero = tk.Entry(ventana)
entry_genero.grid(row=4, column=1, padx=10, pady=10)

entry_alergias = tk.Entry(ventana)
entry_alergias.grid(row=5, column=1, padx=10, pady=10)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_datos)
boton_agregar.grid(row=6, column=0, columnspan=2, pady=10)

# Botón para limpiar los campos
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
boton_limpiar.grid(row=7, column=0, columnspan=2, pady=10)

# Crear una lista para mostrar los datos ingresados
lista_datos = tk.Listbox(ventana, width=60, height=10)
lista_datos.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
