#Ejercicio 6: Validación de Contraseña 
#Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
#Debe tener al menos 8 caracteres de longitud.
#Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
#El programa debe informar al usuario si la contraseña es válida o no.

import re

def validar_contrasena(contrasena):
    # Verificar longitud mínima de 8 caracteres
    if len(contrasena) < 8:
        return False
    
    # Verificar al menos una letra mayúscula
    if not re.search(r'[A-Z]', contrasena):
        return False
    
    # Verificar al menos una letra minúscula
    if not re.search(r'[a-z]', contrasena):
        return False
    
    # Verificar al menos un número
    if not re.search(r'\d', contrasena):
        return False
    
    # Verificar al menos un carácter especial
    if not re.search(r'[!@#$%^&*()-+=]', contrasena):
        return False
    
    return True

# Pedir al usuario que ingrese la contraseña
contrasena = input("Ingrese su contraseña: ")

# Validar la contraseña ingresada
if validar_contrasena(contrasena):
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los requisitos.")