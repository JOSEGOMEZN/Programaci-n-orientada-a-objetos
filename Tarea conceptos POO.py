class Animal:
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo público
        self.__edad = 0  # Atributo privado

    def obtener_edad(self):
        return self.__edad

    def establecer_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa.")

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido general.")

    def describir(self, *caracteristicas):
        descripcion = f"Soy {self.nombre}."
        if caracteristicas:
            descripcion += " Mis características son: " + ", ".join(caracteristicas)
        print(descripcion)

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llamada al constructor de la clase base
        self.raza = raza

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def describir(self, *caracteristicas):
        super().describir(*caracteristicas)
        print(f"Soy un perro de raza {self.raza}.")

animal = Animal("Animalito")
animal.establecer_edad(5)
print(f"Edad de {animal.nombre}: {animal.obtener_edad()} años.")
animal.hacer_sonido()
animal.describir("Imperativo", "Rápido")

perro = Perro("Terry", "Pastor Alemán")
perro.establecer_edad(3)
print(f"Edad de {perro.nombre}: {perro.obtener_edad()} años.")
perro.hacer_sonido()
perro.describir("Leal", "Valiente")
