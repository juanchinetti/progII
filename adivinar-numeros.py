#Ejercicio 11: Adivinador de números
#Crea un juego que le pida al usuario que piense un número entre 1 y 100. 
#Luego, el programa debe intentar adivinar ese número utilizando la estrategia de búsqueda binaria. 
#En cada intento, el programa debe preguntar al usuario si el número a adivinar es mayor, menor o igual al número propuesto por el programa.
#El juego debe terminar cuando el programa adivine el número correcto.


def adivinar_numero():
    print("Piensa en un número entre 1 y 100 y yo trataré de adivinarlo.")
    input("Presiona Enter cuando estés listo para comenzar...")
    
    limite_inferior = 1
    limite_superior = 100
    
    while True:
        numero_propuesto = (limite_inferior + limite_superior) // 2
        respuesta = input(f"¿Es {numero_propuesto} tu número? (mayor/menor/igual): ").lower()
        
        if respuesta == "igual":
            print("¡Hurra! ¡He adivinado tu número!")
            break
        elif respuesta == "mayor":
            limite_inferior = numero_propuesto + 1
        elif respuesta == "menor":
            limite_superior = numero_propuesto - 1
        else:
            print("Por favor, ingresa 'mayor', 'menor' o 'igual'.")

# Inicia el juego
adivinar_numero()