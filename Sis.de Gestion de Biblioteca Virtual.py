# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"'{self.titulo}' de {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

    def listar_libros_prestados(self):
        return [libro.titulo for libro in self.libros_prestados]


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros {ISBN: Libro}
        self.usuarios = {}  # Diccionario de usuarios {ID: Usuario}

    def anadir_libro(self, libro):
        """Añadir un libro a la biblioteca."""
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido con éxito.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        """Quitar un libro de la biblioteca."""
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        """Registrar un nuevo usuario en la biblioteca."""
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        """Eliminar un usuario de la biblioteca."""
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        """Prestar un libro a un usuario."""
        usuario = self.usuarios.get(id_usuario, None)
        libro = self.libros.get(isbn, None)

        if not usuario:
            print(f"Usuario con ID {id_usuario} no encontrado.")
            return
        if not libro:
            print(f"Libro con ISBN {isbn} no encontrado.")
            return
        if libro in usuario.libros_prestados:
            print(f"El usuario {usuario.nombre} ya tiene prestado el libro '{libro.titulo}'.")
            return

        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        """Devolver un libro prestado por un usuario."""
        usuario = self.usuarios.get(id_usuario, None)
        libro = self.libros.get(isbn, None)

        if not usuario:
            print(f"Usuario con ID {id_usuario} no encontrado.")
            return
        if not libro:
            print(f"Libro con ISBN {isbn} no encontrado.")
            return
        if libro not in usuario.libros_prestados:
            print(f"El usuario {usuario.nombre} no tiene prestado el libro '{libro.titulo}'.")
            return

        usuario.libros_prestados.remove(libro)
        print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")

    def buscar_libros(self, **kwargs):
        """Buscar libros por diferentes criterios (título, autor, categoría)."""
        resultados = []
        for libro in self.libros.values():
            if all(getattr(libro, k, None) == v for k, v in kwargs.items()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self):
        """Listar todos los libros prestados por los usuarios."""
        prestamos = {}
        for usuario in self.usuarios.values():
            libros_prestados = usuario.listar_libros_prestados()
            if libros_prestados:
                prestamos[usuario.nombre] = libros_prestados
        return prestamos


# Función para mostrar el menú interactivo
def mostrar_menu():
    print("\n----- Menú Biblioteca -----")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libros")
    print("8. Listar libros prestados")
    print("9. Salir")


# Función para interactuar con el sistema
def interactuar():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-9): ")

        if opcion == '1':  # Añadir libro
            titulo = input("Introduce el título del libro: ")
            autor = input("Introduce el autor del libro: ")
            categoria = input("Introduce la categoría del libro: ")
            isbn = input("Introduce el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.anadir_libro(libro)

        elif opcion == '2':  # Quitar libro
            isbn = input("Introduce el ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == '3':  # Registrar usuario
            nombre = input("Introduce el nombre del usuario: ")
            id_usuario = input("Introduce el ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '4':  # Dar de baja usuario
            id_usuario = input("Introduce el ID del usuario a dar de baja: ")
            biblioteca.dar_de_baja_usuario(id_usuario)

        elif opcion == '5':  # Prestar libro
            id_usuario = input("Introduce el ID del usuario: ")
            isbn = input("Introduce el ISBN del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == '6':  # Devolver libro
            id_usuario = input("Introduce el ID del usuario: ")
            isbn = input("Introduce el ISBN del libro: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == '7':  # Buscar libros
            criterio = input("Buscar por título, autor o categoría? (título/autor/categoría): ").lower()
            valor = input(f"Introduce el valor para buscar por {criterio}: ")
            if criterio == "titulo":
                resultados = biblioteca.buscar_libros(titulo=valor)
            elif criterio == "autor":
                resultados = biblioteca.buscar_libros(autor=valor)
            elif criterio == "categoria":
                resultados = biblioteca.buscar_libros(categoria=valor)
            else:
                print("Criterio no válido.")
                continue

            if resultados:
                print("Libros encontrados:")
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros con esos criterios.")

        elif opcion == '8':  # Listar libros prestados
            prestamos = biblioteca.listar_libros_prestados()
            if prestamos:
                print("Libros prestados:")
                for usuario, libros in prestamos.items():
                    print(f"{usuario}: {', '.join(libros)}")
            else:
                print("No hay libros prestados actualmente.")

        elif opcion == '9':  # Salir
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor selecciona una opción entre 1 y 9.")


# Ejecutar la función de interacción
interactuar()






