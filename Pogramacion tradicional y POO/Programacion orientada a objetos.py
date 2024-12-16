class Clima:
    def __init__(self):
        self.__temperaturas = []  # Atributo privado para almacenar las temperaturas

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for dia in range(1, 8):  # 7 días en la semana
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para el día {dia}: "))
                    self.__temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido para la temperatura.")

    # Método para calcular el promedio semanal de las temperaturas
    def calcular_promedio(self):
        if len(self.__temperaturas) == 7:  # Verifica que se hayan ingresado las 7 temperaturas
            promedio = sum(self.__temperaturas) / len(self.__temperaturas)
            return promedio
        else:
            return 0.0

    # Método para mostrar la información del clima (temperaturas y promedio)
    def mostrar_informacion(self):
        print(f"Temperaturas de la semana: {self.__temperaturas}")
        print(f"Promedio semanal de las temperaturas: {self.calcular_promedio():.2f}°C")


# Clase derivada que agrega la funcionalidad de humedad
class ClimaConHumedad(Clima):
    def __init__(self):
        super().__init__()  # Llamada al constructor de la clase base
        self.__humedades = []  # Atributo privado para almacenar las humedades

    # Método para ingresar las temperaturas y humedades diarias
    def ingresar_datos(self):
        for dia in range(1, 8):  # 7 días en la semana
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para el día {dia}: "))
                    humedad = float(input(f"Ingrese la humedad para el día {dia} (%): "))
                    self.__temperaturas.append(temp)
                    self.__humedades.append(humedad)
                    break
                except ValueError:
                    print("Por favor, ingrese valores numéricos válidos para la temperatura y humedad.")

    # Método para calcular el promedio semanal de las temperaturas y humedades
    def calcular_promedio(self):
        if len(self.__temperaturas) == 7:
            promedio_temp = sum(self.__temperaturas) / len(self.__temperaturas)
            promedio_humedad = sum(self.__humedades) / len(self.__humedades)
            return promedio_temp, promedio_humedad
        else:
            return 0.0, 0.0

    # Método para mostrar la información del clima con temperatura y humedad
    def mostrar_informacion(self):
        promedio_temp, promedio_humedad = self.calcular_promedio()
        print(f"Temperaturas de la semana: {self.__temperaturas}")
        print(f"Humedades de la semana: {self.__humedades}")
        print(f"Promedio semanal de las temperaturas: {promedio_temp:.2f}°C")
        print(f"Promedio semanal de la humedad: {promedio_humedad:.2f}%")


# Función principal
def main():
    print("Sistema de registro de clima")

    # Usamos la clase Clima para ingresar solo temperaturas
    clima = Clima()
    clima.ingresar_temperaturas()
    clima.mostrar_informacion()

    # Usamos la clase ClimaConHumedad para ingresar temperaturas y humedades
    clima_humedad = ClimaConHumedad()
    clima_humedad.ingresar_datos()
    clima_humedad.mostrar_informacion()


if __name__ == "__main__":
    main()
