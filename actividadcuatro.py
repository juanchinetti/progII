#Ejercicio 4: Contador de Palabras

# Solicitar al usuario que ingrese una frase
frase = input("Ingrese una frase: ")

# Contar el número de palabras en la frase
palabras = frase.split()
num_palabras = len(palabras)

# Mostrar el número de palabras en la frase
print("El número de palabras en la frase es:", num_palabras)