import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Función cuadrática
def f(x, a, b, c):
    return a * x**2 + b * x + c

# Ingreso de datos
a = float(input("Ingrese el valor de a (coeficiente cuadrático): "))
b = float(input("Ingrese el valor de b (coeficiente lineal): "))
c = float(input("Ingrese el valor de c (término independiente): "))
x_start = float(input("Ingrese el valor inicial del intervalo: "))
x_end = float(input("Ingrese el valor final del intervalo: "))
n_rect = int(input("Ingrese la cantidad de rectángulos para la aproximación: "))

# Calcular el ancho de cada rectángulo
width = (x_end - x_start) / n_rect

# Inicializar las sumas
sum_inferior = 0
sum_superior = 0

# Calcular las sumas inferior y superior
for i in range(n_rect):
    x_i = x_start + i * width
    x_next = x_start + (i + 1) * width
    sum_inferior += f(x_i, a, b, c) * width
    sum_superior += f(x_next, a, b, c) * width

# Calcular el área real usando la integración numérica con quad
area_real, _ = quad(f, x_start, x_end, args=(a, b, c))

# Calcular el error relativo para ambas sumas
error_inferior = abs((area_real - sum_inferior) / area_real) * 100
error_superior = abs((area_real - sum_superior) / area_real) * 100

# Mostrar los resultados
print("\nResultados:")
print(f"Suma inferior: {sum_inferior:.4f}")
print(f"Suma superior: {sum_superior:.4f}")
print(f"Área real: {area_real:.4f}")
print(f"Error relativo suma inferior: {error_inferior:.4f}%")
print(f"Error relativo suma superior: {error_superior:.4f}%")

# Graficar la función cuadrática y los rectángulos de aproximación
x = np.linspace(x_start - 1, x_end + 1, 400)  # Puntos para la curva
y = f(x, a, b, c)

# Gráfica de la parábola
plt.plot(x, y, label='f(x) = ax² + bx + c', color='blue')
plt.title('Gráfica de la función cuadrática y las sumas de Riemann')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)

# Graficar rectángulos para la suma inferior (en verde)
for i in range(n_rect):
    plt.bar(x_start + i * width, f(x_start + i * width, a, b, c), width=width, align='edge', alpha=0.3, color='green')

# Graficar rectángulos para la suma superior (en rojo)
for i in range(n_rect):
    plt.bar(x_start + (i + 1) * width, f(x_start + (i + 1) * width, a, b, c), width=width, align='edge', alpha=0.3, color='red')

plt.legend()
plt.grid(True)
plt.show()