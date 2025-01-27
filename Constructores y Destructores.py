class Archivo:
    # Constructor
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        try:
            # Intentamos abrir el archivo en modo escritura
            self.archivo = open(self.nombre_archivo, 'w')
            print(f"Archivo '{self.nombre_archivo}' abierto exitosamente.")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            self.archivo = None

    # Método para escribir en el archivo
    def escribir(self, texto):
        if self.archivo:
            self.archivo.write(texto)
            print(f"Texto escrito en '{self.nombre_archivo}': {texto}")
        else:
            print("El archivo no se ha abierto correctamente.")

    # Destructor
    def __del__(self):
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")
        else:
            print("No se pudo cerrar el archivo porque no se abrió correctamente.")


# Crear un objeto de la clase Archivo
archivo1 = Archivo("mi_archivo.txt")
archivo1.escribir("Hola, este es un ejemplo de uso de constructores y destructores.")
del archivo1  # Llamada explícita al destructor (aunque el destructor se llama automáticamente al finalizar)

# Crear otro objeto para ver cómo se maneja otro archivo
archivo2 = Archivo("otro_archivo.txt")
archivo2.escribir("Este es otro archivo de prueba.")
