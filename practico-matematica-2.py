def convertir_tiempo_a_decimal(tiempo):
    """
    Convertir tiempo en formato HH:MM a decimal.
    """
    horas, minutos = map(int, tiempo.split(':'))
    return horas + minutos / 60

def calcular_cuartiles(datos):
    """
    Calcular cuartiles de una lista de datos.
    """
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    q1_idx = (n + 1) // 4
    q2_idx = (n + 1) // 2
    q3_idx = 3 * (n + 1) // 4
    
    q1 = datos_ordenados[q1_idx - 1]
    q2 = datos_ordenados[q2_idx - 1]
    q3 = datos_ordenados[q3_idx - 1]
    
    return q1, q2, q3

def calcular_media(datos):
    """
    Calcular la media de una lista de datos.
    """
    return sum(datos) / len(datos)

def calcular_varianza(datos):
    """
    Calcular la varianza de una lista de datos.
    """
    media = calcular_media(datos)
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    return suma_cuadrados / (len(datos) - 1)

def calcular_raiz_cuadrada(valor):
    """
    Calcular la raíz cuadrada de un valor sin usar math.sqrt().
    """
    # Método de aproximación de Newton
    if valor == 0:
        return 0
    aproximacion = valor
    while True:
        mejor_aprox = (aproximacion + valor / aproximacion) / 2
        if abs(aproximacion - mejor_aprox) < 1e-10:
            return mejor_aprox
        aproximacion = mejor_aprox

def calcular_desviacion_estandar(datos):
    """
    Calcular la desviación estándar de una lista de datos.
    """
    return calcular_raiz_cuadrada(calcular_varianza(datos))

def calcular_factorial(n):
    """
    Calcular el factorial de un número n sin usar math.factorial().
    """
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def calcular_combinaciones(n, x):
    """
    Calcular combinaciones (nCx) sin usar math.comb().
    """
    return calcular_factorial(n) / (calcular_factorial(x) * calcular_factorial(n - x))

def calcular_probabilidad_binomial(n, p, x):
    """
    Calcular probabilidad binomial.
    """
    if not (0 <= p <= 1):
        return "Error: La probabilidad de éxito (p) debe estar entre 0 y 1."
    if x > n:
        return "Error: El número de éxitos (x) no puede ser mayor que el número de ensayos (n)."
    
    combinaciones = calcular_combinaciones(n, x)
    probabilidad = combinaciones * (p ** x) * ((1 - p) ** (n - x))
    return probabilidad

def calcular_probabilidad_acumulada_binomial(n, p, x):
    """
    Calcular la probabilidad acumulada binomial.
    """
    probabilidad_acumulada = 0
    for i in range(x + 1):
        probabilidad_acumulada += calcular_probabilidad_binomial(n, p, i)
    return probabilidad_acumulada

def calcular_medidas(datos, opciones):
    """
    Calcular medidas estadísticas de una lista de datos según las opciones seleccionadas.
    """
    resultados = {}
    if 1 in opciones:
        resultados['Media'] = calcular_media(datos)
    if 2 in opciones:
        resultados['Mediana'] = sorted(datos)[len(datos) // 2]
    if 3 in opciones:
        moda = max(set(datos), key=datos.count)
        if datos.count(moda) == 1:
            resultados['Moda'] = "No hay moda"
        else:
            resultados['Moda'] = moda
    if 4 in opciones:
        cuartiles = calcular_cuartiles(datos)
        resultados['Cuartiles'] = cuartiles
    if 5 in opciones:
        resultados['Rango'] = max(datos) - min(datos)
    if 6 in opciones:
        resultados['Varianza'] = calcular_varianza(datos)
    if 7 in opciones:
        resultados['Desviación estándar'] = calcular_desviacion_estandar(datos)
    return resultados

def mostrar_resultados(resultados):
    """
    Mostrar resultados de las medidas estadísticas.
    """
    print("\nResultados:")
    for medida, valor in resultados.items():
        if isinstance(valor, tuple):
            print(f"{medida}: Q1 = {valor[0]:.2f}, Q2 (Mediana) = {valor[1]:.2f}, Q3 = {valor[2]:.2f}")
        else:
            print(f"{medida}: {valor}")

def menu_probabilidad():
    """
    Menú de probabilidad.
    """
    print("Probabilidad")
    print("1. Binomial")
    print("2. Poisson")
    print("3. Hipergeométrica")
    print("4. Gaussiana")
    
    opcion = int(input("Ingrese la opción: "))
    acumulativa = input("¿Desea calcular la probabilidad acumulada? (s/n): ").lower() == 's'
    
    if opcion == 1:
        n = int(input("Ingrese el número de ensayos (n): "))
        p = float(input("Ingrese la probabilidad de éxito (p): "))
        x = int(input("Ingrese el número de éxitos (x): "))
        if acumulativa:
            resultado = calcular_probabilidad_acumulada_binomial(n, p, x)
        else:
            resultado = calcular_probabilidad_binomial(n, p, x)
    elif opcion == 2:
        print("Función no implementada")
    elif opcion == 3:
        print("Función no implementada")
    elif opcion == 4:
        print("Función no implementada")
    else:
        print("Opción inválida")
        return
    
    tipo = "acumulada" if acumulativa else "puntual"
    print(f"La probabilidad {tipo} es: {resultado:.4f}")

def main():
    while True:
        print("Menú Principal")
        print("1. Probabilidad")
        print("2. Estadística")
        print("3. Salir")
        
        opcion = int(input("Ingrese la opción: "))
        
        if opcion == 1:
            menu_probabilidad()
        elif opcion == 2:
            print("Función no implementada")
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()