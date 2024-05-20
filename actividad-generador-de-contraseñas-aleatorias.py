#Ejercicio 8: Generador de Contraseñas Aleatorias 
#Escribe un programa en Python que genere una contraseña aleatoria para el usuario.
#La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de letras (mayúsculas y minúsculas), números y caracteres especiales.
#El programa debe mostrar la contraseña generada al usuario.

import random
import string

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud_minima = 12

print("Generador de Contraseñas Aleatorias")
print("------------------------------------")

while True:
    longitud = int(input("Ingrese la longitud de la contraseña (mínimo 12 caracteres): "))
    if longitud >= longitud_minima:
        break
    else:
        print(f"La longitud mínima de la contraseña debe ser {longitud_minima} caracteres o más.")

nueva_contrasena = generar_contrasena(longitud)
print("La contraseña generada es:", nueva_contrasena)