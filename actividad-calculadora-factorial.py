#Ejercicio 9: Calculadora de Factorial 
#Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario.
#El factorial de un número entero positivo n se define como el producto de todos los enteros positivos menores o iguales a n.
#El programa debe manejar números enteros grandes y mostrar el resultado.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

try:
    numero = int(input("Ingrese un número entero para calcular su factorial: "))
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        resultado = factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")