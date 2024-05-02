#Ejercicio 5: Conversor de Temperatura (Actualización)

# Solicitar al usuario que elija la conversión deseada
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
opcion = int(input("Ingrese su opción (1 o 2): "))

# Según la opción elegida, solicitar la temperatura y realizar la conversión
if opcion == 1:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("La temperatura en grados Fahrenheit es:", fahrenheit)
elif opcion == 2:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("La temperatura en grados Celsius es:", celsius)
else:
    print("Opción no válida. Por favor, ingrese 1 o 2.")