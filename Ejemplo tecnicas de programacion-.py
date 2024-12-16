from abc import ABC, abstractmethod


# Clase base abstracta
class Vehiculo(ABC):

    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def detener(self):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass


# Clase concreta: Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} ha arrancado.")

    def detener(self):
        print(f"El coche {self.marca} {self.modelo} se ha detenido.")

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


# Clase concreta: Camion
class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad

    def arrancar(self):
        print(f"El camión {self.marca} {self.modelo} ha arrancado.")

    def detener(self):
        print(f"El camión {self.marca} {self.modelo} se ha detenido.")

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Capacidad: {self.capacidad} toneladas")


# Ejemplo de uso
def gestionar_vehiculo(vehiculo: Vehiculo):
    vehiculo.arrancar()
    vehiculo.mostrar_informacion()
    vehiculo.detener()


# Crear instancias de Coche y Camión
mi_coche = Coche("Toyota", "Corolla")
mi_camion = Camion("Volvo", "FH", 18)

# Gestionar vehículos utilizando la abstracción
gestionar_vehiculo(mi_coche)
gestionar_vehiculo(mi_camion)
