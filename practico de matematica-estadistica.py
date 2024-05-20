#trabajo practico de matematica 
#Ingresar por teclado los datos a analizar.
#Seleccionar de algún modo las medidas de posición y dispersión que el usuario desea visualizar.
#Escalabilidad. La programación deberá permitir que se agreguen funcionalidades a medida que se avance  en el desarrollo del espacio curricular.
#Además en futuros trabajos partirán de producciones realizadas por sus compañeros, por lo que es una buena práctica la documentación del software.

import numpy as np

def calcular_moda(data):
    # Calcula la moda o modas de los datos
    frecuencias = {}
    for valor in data:
        if valor in frecuencias:
            frecuencias[valor] += 1
        else:
            frecuencias[valor] = 1
    
    max_frecuencia = max(frecuencias.values())
    modas = [k for k, v in frecuencias.items() if v == max_frecuencia]
    
    return modas

# Preguntar al usuario por la categoría de los datos
print("Seleccione la categoría de los datos:")
print("1. Peso (Kg, Libras, etc)")
print("2. Distancia (Metros, Pies, etc)")
print("3. Tiempo (Horas, Minutos, Segundos, etc)")
print("4. Precios")
categoria = input("Ingrese el número de la categoría: ")

# Asignar la unidad basada en la categoría seleccionada
unidad = ""
if categoria == "1":
    unidad = input("Ingrese la unidad de peso (por ejemplo, Kg, Libras): ")
elif categoria == "2":
    unidad = input("Ingrese la unidad de distancia (por ejemplo, Metros, Pies): ")
elif categoria == "3":
    unidad = input("Ingrese la unidad de tiempo (por ejemplo, Horas, Minutos, Segundos): ")
elif categoria == "4":
    unidad = input("Ingrese la moneda (por ejemplo, USD, EUR): ")
else:
    print("Categoría no válida. Saliendo del programa.")
    exit()

# Preguntar al usuario por los datos
data = sorted(list(map(float, input(f"Ingrese los datos en {unidad} separados por espacios: ").split())))

# Preguntar al usuario qué estadísticas desea ver
print("Seleccione las estadísticas que desea ver (puede seleccionar varias separadas por comas):")
print("1. Media")
print("2. Mediana")
print("3. Moda")
print("4. Desviación Estándar")
print("5. Varianza")
print("6. Rango")
print("7. Cuartiles (Q1, Q2, Q3)")
opciones = input("Ingrese los números de las estadísticas que desea ver: ").split(',')

# Mostrar las estadísticas seleccionadas
if "1" in opciones:
    print(f"La Media de este conjunto es: {np.mean(data)} {unidad}")

if "2" in opciones:
    print(f"La Mediana de este conjunto es: {np.median(data)} {unidad}")

if "3" in opciones:
    modas = calcular_moda(data)
    if len(modas) == 1:
        print(f"La Moda de este conjunto es: {modas[0]} {unidad}")
    elif len(modas) > 1:
        print(f"Las Modas de este conjunto son: {', '.join(map(str, modas))} {unidad}")
    else:
        print("No hay una moda en este conjunto de datos")

if "4" in opciones:
    print(f"La Desviación Estándar de este conjunto es: {np.std(data)} {unidad}")

if "5" in opciones:
    print(f"La Varianza de Este Conjunto es: {np.var(data)} {unidad}")

if "6" in opciones:
    print(f"El Rango de este conjunto es: {np.max(data) - np.min(data)} {unidad}")

if "7" in opciones:
    print(f"Q1: {np.percentile(data, 25)} {unidad}")
    print(f"Q2 (Mediana): {np.percentile(data, 50)} {unidad}")
    print(f"Q3: {np.percentile(data, 75)} {unidad}")

        