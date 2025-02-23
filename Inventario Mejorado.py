class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}$"

    # Representación para almacenar en archivo
    def to_file(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"

    # Crear producto desde archivo
    @staticmethod
    def from_file(line):
        id, nombre, cantidad, precio = line.strip().split(',')
        return Producto(id, nombre, int(cantidad), float(precio))


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    # Cargar productos desde archivo
    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for line in file:
                    producto = Producto.from_file(line)
                    self.productos.append(producto)
        except FileNotFoundError:
            print("Archivo no encontrado, creando un nuevo archivo.")
        except PermissionError:
            print("Error de permisos al intentar abrir el archivo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    # Guardar productos al archivo
    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(producto.to_file())
        except PermissionError:
            print("Error de permisos al intentar guardar el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    # Añadir producto, asegurándonos de que el ID sea único
    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print(f"Producto {producto.get_nombre()} añadido al inventario.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            self.guardar_inventario()
            print(f"Producto {producto.get_nombre()} eliminado del inventario.")
        else:
            print("Producto no encontrado.")

    # Actualizar cantidad o precio de un producto por ID
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()
            print(f"Producto {producto.get_nombre()} actualizado.")
        else:
            print("Producto no encontrado.")

    # Buscar producto por nombre (puede haber nombres similares)
    def buscar_producto_por_nombre(self, nombre):
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for p in productos_encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    # Buscar producto por ID
    def buscar_producto_por_id(self, id_producto):
        return next((p for p in self.productos if p.get_id() == id_producto), None)

    # Mostrar todos los productos
    def mostrar_productos(self):
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()

    while True:
        print("\n---- Menú de Gestión de Inventarios ----")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todos los Productos")
        print("6. Salir")

        try:
            opcion = int(input("Elige una opción (1-6): "))

            if opcion == 1:
                # Añadir producto
                id_producto = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad del producto: "))
                precio = float(input("Precio del producto ($): "))
                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo_producto)

            elif opcion == 2:
                # Eliminar producto
                id_producto = input("ID del producto a eliminar: ")
                inventario.eliminar_producto(id_producto)

            elif opcion == 3:
                # Actualizar producto
                id_producto = input("ID del producto a actualizar: ")
                cantidad = input("Nueva cantidad (deja en blanco si no quieres actualizarla): ")
                precio = input("Nuevo precio ($) (deja en blanco si no quieres actualizarlo): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == 4:
                # Buscar producto por nombre
                nombre = input("Nombre del producto a buscar: ")
                inventario.buscar_producto_por_nombre(nombre)

            elif opcion == 5:
                # Mostrar todos los productos
                inventario.mostrar_productos()

            elif opcion == 6:
                print("¡Hasta luego!")
                break

            else:
                print("Opción inválida. Por favor, elige una opción entre 1 y 6.")

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")


# Ejecutar el menú
menu()
