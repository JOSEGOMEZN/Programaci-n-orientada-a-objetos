import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos de acceso
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos de actualización
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}  # Usamos un diccionario para almacenar productos por su ID

    # Método para añadir un nuevo producto
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Producto con ese ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print(f"Producto '{producto.get_nombre()}' añadido al inventario.")

    # Método para eliminar un producto por su ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado del inventario.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    # Método para actualizar la cantidad de un producto
    def actualizar_cantidad(self, id_producto, cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].set_cantidad(cantidad)
            print(f"Cantidad de producto {id_producto} actualizada a {cantidad}.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    # Método para actualizar el precio de un producto
    def actualizar_precio(self, id_producto, precio):
        if id_producto in self.productos:
            self.productos[id_producto].set_precio(precio)
            print(f"Precio de producto {id_producto} actualizado a {precio}.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    # Método para buscar un producto por nombre
    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos.values() if
                       nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    # Método para mostrar todos los productos
    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    # Función para guardar el inventario en un archivo JSON
    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id_producto: producto.__dict__ for id_producto, producto in self.productos.items()}, f)
            print(f"Inventario guardado en {archivo}.")

    # Función para cargar el inventario desde un archivo JSON
    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                for id_producto, producto_data in data.items():
                    producto = Producto(producto_data['id_producto'], producto_data['nombre'],
                                        producto_data['cantidad'], producto_data['precio'])
                    self.productos[id_producto] = producto
                print(f"Inventario cargado desde {archivo}.")
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe.")


def menu():
    inventario = Inventario()

    # Cargar inventario desde archivo si existe
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Cantidad de Producto")
        print("4. Actualizar Precio de Producto")
        print("5. Buscar Producto por Nombre")
        print("6. Mostrar Todo el Inventario")
        print("7. Guardar Inventario")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar cantidad: ")
            cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(id_producto, cantidad)

        elif opcion == "4":
            id_producto = input("ID del producto a actualizar precio: ")
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_precio(id_producto, precio)

        elif opcion == "5":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "6":
            inventario.mostrar_inventario()

        elif opcion == "7":
            inventario.guardar_en_archivo("inventario.json")

        elif opcion == "8":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()
