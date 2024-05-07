#Ejercicio 7: Juego de Adivinar el Número 
#Desarrolla un juego en el que el programa selecciona aleatoriamente un número entre 1 y 100 y el jugador debe adivinarlo.
#El programa debe proporcionar pistas al jugador si el número ingresado es demasiado alto o demasiado bajo.
#El juego debe continuar hasta que el jugador adivine correctamente el número.

import random

def juego_adivinar_numero():
    numero_a_adivinar = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de Adivinar el Número!")
    print("Tienes que adivinar un número entre 1 y 100.")

    while True:
        intento = int(input("Introduce tu intento: "))
        intentos += 1

        if intento < numero_a_adivinar:
            print("El número es demasiado bajo. Inténtalo de nuevo.")
        elif intento > numero_a_adivinar:
            print("El número es demasiado alto. Inténtalo de nuevo.")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
            break

# Llama a la función para iniciar el juego
juego_adivinar_numero()

