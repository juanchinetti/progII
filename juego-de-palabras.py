#Ejercicio 10: Juego del Ahorcado 

import random

def elegir_palabra():
    palabras = ["python", "programacion", "ordenador", "inteligencia", "computadora", "algoritmo", "desarrollo", "aplicacion"]
    return random.choice(palabras)

def mostrar_tablero(palabra_oculta, letras_adivinadas):
    tablero = ""
    for letra in palabra_oculta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero

def jugar_ahorcado():
    palabra_oculta = elegir_palabra()
    intentos_maximos = 6
    letras_adivinadas = []
    letras_intentadas = []
    
    print("¡Bienvenido al Juego del Ahorcado!")
    print("Adivina la palabra oculta. Tienes", intentos_maximos, "intentos.")

    while intentos_maximos > 0:
        tablero = mostrar_tablero(palabra_oculta, letras_adivinadas)
        print(tablero)
        if "_" not in tablero:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break
        
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_intentadas:
            print("Ya has intentado con esa letra. Intenta con otra.")
            continue

        letras_intentadas.append(letra)

        if letra in palabra_oculta:
            letras_adivinadas.append(letra)
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            intentos_maximos -= 1
            print("Letra incorrecta. Te quedan", intentos_maximos, "intentos.")

    if "_" in mostrar_tablero(palabra_oculta, letras_adivinadas):
        print("¡Oh no! Te has quedado sin intentos. La palabra era:", palabra_oculta)


jugar_ahorcado()