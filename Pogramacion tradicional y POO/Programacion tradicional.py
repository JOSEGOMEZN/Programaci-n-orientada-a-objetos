# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(1, 8):  # 7 días en una semana
        while True:
            try:
                temp = float(input(f"Introduce la temperatura del día {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingresa un número válido para la temperatura.")
    return temperaturas

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio_semanal(temperaturas):
    total = sum(temperaturas)  # Suma de todas las temperaturas
    promedio = total / len(temperaturas)  # División entre la cantidad de días (7)
    return promedio

# Función para mostrar los resultados
def mostrar_resultados(promedio):
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} grados.")

# Función principal que organiza el flujo del programa
def main():
    print("Bienvenido al sistema de registro de temperaturas.")
    # Obtener las temperaturas de la semana
    temperaturas = ingresar_temperaturas()
    # Calcular el promedio
    promedio = calcular_promedio_semanal(temperaturas)
    # Mostrar el resultado
    mostrar_resultados(promedio)

# Llamar a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
