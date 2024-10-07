import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Variables globales para los entries de matrices
entry_a1 = entry_b1 = entry_c1 = entry_d1 = None
entry_a2 = entry_b2 = entry_c2 = entry_d2 = None
entry_a3 = entry_b3 = entry_c3 = entry_d3 = None

def gauss_jordan(matrix):
    n = len(matrix)

    # Aplicar el método de Gauss-Jordan
    for i in range(n):
        matrix[i] = matrix[i] / matrix[i][i]
        for j in range(n):
            if i != j:
                matrix[j] = matrix[j] - matrix[i] * matrix[j][i]

    return matrix

def calcular_matriz_2x2():
    try:
        a1 = float(entry_a1.get())
        b1 = float(entry_b1.get())
        c1 = float(entry_c1.get())
        a2 = float(entry_a2.get())
        b2 = float(entry_b2.get())
        c2 = float(entry_c2.get())

        matrix = np.array([[a1, b1, c1],
                           [a2, b2, c2]])

        resultado = gauss_jordan(matrix)

        if np.allclose(resultado[:, -1], resultado[0][-1]) and np.allclose(resultado[:, -1], resultado[1][-1]):
            x, y = resultado[0][2], resultado[1][2]
            messagebox.showinfo("Resultado", f"Sistema Compatible Determinado\nx = {x:.2f}, y = {y:.2f}")
        else:
            messagebox.showinfo("Resultado", "Sistema Incompatible")

        # Mostrar gráfico
        plt.figure()
        x_vals = np.linspace(-10, 10, 100)
        y1 = (c1 - a1 * x_vals) / b1
        y2 = (c2 - a2 * x_vals) / b2
        plt.plot(x_vals, y1, label='Ecuación 1')
        plt.plot(x_vals, y2, label='Ecuación 2')
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.title('Gráfico de las Ecuaciones 2x2')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid()
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

def calcular_matriz_3x3():
    try:
        a1 = float(entry_a1.get())
        b1 = float(entry_b1.get())
        c1 = float(entry_c1.get())
        d1 = float(entry_d1.get())
        a2 = float(entry_a2.get())
        b2 = float(entry_b2.get())
        c2 = float(entry_c2.get())
        d2 = float(entry_d2.get())
        a3 = float(entry_a3.get())
        b3 = float(entry_b3.get())
        c3 = float(entry_c3.get())
        d3 = float(entry_d3.get())

        matrix = np.array([[a1, b1, c1, d1],
                           [a2, b2, c2, d2],
                           [a3, b3, c3, d3]])

        resultado = gauss_jordan(matrix)

        if np.allclose(resultado[:, -1], resultado[0][-1]) and np.allclose(resultado[:, -1], resultado[1][-1]) and np.allclose(resultado[:, -1], resultado[2][-1]):
            x, y, z = resultado[0][3], resultado[1][3], resultado[2][3]
            messagebox.showinfo("Resultado", f"Sistema Compatible Determinado\nx = {x:.2f}, y = {y:.2f}, z = {z:.2f}")
        else:
            messagebox.showinfo("Resultado", "Sistema Incompatible")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

def matrices_2x2():
    clear_frame()
    global entry_a1, entry_b1, entry_c1, entry_a2, entry_b2, entry_c2
    tk.Label(frame_matrices, text="Ecuación 1:").grid(row=0, column=0)
    entry_a1 = tk.Entry(frame_matrices)
    entry_a1.grid(row=0, column=1)

    entry_b1 = tk.Entry(frame_matrices)
    entry_b1.grid(row=0, column=2)

    entry_c1 = tk.Entry(frame_matrices)
    entry_c1.grid(row=0, column=3)

    tk.Label(frame_matrices, text="Ecuación 2:").grid(row=1, column=0)
    entry_a2 = tk.Entry(frame_matrices)
    entry_a2.grid(row=1, column=1)

    entry_b2 = tk.Entry(frame_matrices)
    entry_b2.grid(row=1, column=2)

    entry_c2 = tk.Entry(frame_matrices)
    entry_c2.grid(row=1, column=3)

    tk.Button(frame_matrices, text="Calcular", command=calcular_matriz_2x2).grid(row=2, column=0, columnspan=4)

def matrices_3x3():
    clear_frame()
    global entry_a1, entry_b1, entry_c1, entry_d1
    global entry_a2, entry_b2, entry_c2, entry_d2
    global entry_a3, entry_b3, entry_c3, entry_d3

    tk.Label(frame_matrices, text="Ecuación 1:").grid(row=0, column=0)
    entry_a1 = tk.Entry(frame_matrices)
    entry_a1.grid(row=0, column=1)

    entry_b1 = tk.Entry(frame_matrices)
    entry_b1.grid(row=0, column=2)

    entry_c1 = tk.Entry(frame_matrices)
    entry_c1.grid(row=0, column=3)

    entry_d1 = tk.Entry(frame_matrices)
    entry_d1.grid(row=0, column=4)

    tk.Label(frame_matrices, text="Ecuación 2:").grid(row=1, column=0)
    entry_a2 = tk.Entry(frame_matrices)
    entry_a2.grid(row=1, column=1)

    entry_b2 = tk.Entry(frame_matrices)
    entry_b2.grid(row=1, column=2)

    entry_c2 = tk.Entry(frame_matrices)
    entry_c2.grid(row=1, column=3)

    entry_d2 = tk.Entry(frame_matrices)
    entry_d2.grid(row=1, column=4)

    tk.Label(frame_matrices, text="Ecuación 3:").grid(row=2, column=0)
    entry_a3 = tk.Entry(frame_matrices)
    entry_a3.grid(row=2, column=1)

    entry_b3 = tk.Entry(frame_matrices)
    entry_b3.grid(row=2, column=2)

    entry_c3 = tk.Entry(frame_matrices)
    entry_c3.grid(row=2, column=3)

    entry_d3 = tk.Entry(frame_matrices)
    entry_d3.grid(row=2, column=4)

    tk.Button(frame_matrices, text="Calcular", command=calcular_matriz_3x3).grid(row=3, column=0, columnspan=5)

def calcular_probabilidades():
    messagebox.showinfo("Calculadora de Probabilidades", "Aquí va la calculadora de probabilidades.")

def sumas_riemann():
    def calcular_sumas_riemann():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            x_start = float(entry_x_start.get())
            x_end = float(entry_x_end.get())
            n_rect = int(entry_n_rect.get())

            # Calcular el ancho de cada rectángulo
            width = (x_end - x_start) / n_rect
            sum_inferior = 0
            sum_superior = 0

            # Calcular las sumas inferior y superior
            for i in range(n_rect):
                x_i = x_start + i * width
                x_next = x_start + (i + 1) * width
                sum_inferior += f(x_i, a, b, c) * width
                sum_superior += f(x_next, a, b, c) * width

            # Calcular el área real
            area_real, _ = quad(f, x_start, x_end, args=(a, b, c))

            # Mostrar resultados
            messagebox.showinfo("Resultados",
                                f"Suma inferior: {sum_inferior:.4f}\n"
                                f"Suma superior: {sum_superior:.4f}\n"
                                f"Área real: {area_real:.4f}")

            # Graficar
            x = np.linspace(x_start - 1, x_end + 1, 100)
            y = f(x, a, b, c)
            plt.plot(x, y, label=f"y = {a}x² + {b}x + {c}")
            plt.fill_between(x, y, where=[x_start <= x_ <= x_end for x_ in x], alpha=0.3)

            # Graficar rectángulos
            for i in range(n_rect):
                x_i = x_start + i * width
                x_next = x_start + (i + 1) * width
                plt.bar(x_i, f(x_i, a, b, c), width=width, align='edge', edgecolor='black')

            plt.axhline(0, color='black', lw=0.5)
            plt.axvline(0, color='black', lw=0.5)
            plt.title('Sumas de Riemann')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend()
            plt.grid(True)
            plt.show()

        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos.")

    def f(x, a, b, c):
        return a * x ** 2 + b * x + c

    clear_frame()

    tk.Label(frame_sumas, text="Ingrese los coeficientes de la función cuadrática:").grid(row=0, column=0, columnspan=2)
    tk.Label(frame_sumas, text="a:").grid(row=1, column=0)
    entry_a = tk.Entry(frame_sumas)
    entry_a.grid(row=1, column=1)

    tk.Label(frame_sumas, text="b:").grid(row=2, column=0)
    entry_b = tk.Entry(frame_sumas)
    entry_b.grid(row=2, column=1)

    tk.Label(frame_sumas, text="c:").grid(row=3, column=0)
    entry_c = tk.Entry(frame_sumas)
    entry_c.grid(row=3, column=1)

    tk.Label(frame_sumas, text="Ingrese los límites de integración:").grid(row=4, column=0, columnspan=2)
    tk.Label(frame_sumas, text="x inicio:").grid(row=5, column=0)
    entry_x_start = tk.Entry(frame_sumas)
    entry_x_start.grid(row=5, column=1)

    tk.Label(frame_sumas, text="x fin:").grid(row=6, column=0)
    entry_x_end = tk.Entry(frame_sumas)
    entry_x_end.grid(row=6, column=1)

    tk.Label(frame_sumas, text="Número de rectángulos:").grid(row=7, column=0)
    entry_n_rect = tk.Entry(frame_sumas)
    entry_n_rect.grid(row=7, column=1)

    tk.Button(frame_sumas, text="Calcular", command=calcular_sumas_riemann).grid(row=8, column=0, columnspan=2)

def clear_frame():
    for widget in frame_matrices.winfo_children():
        widget.destroy()

def menu_principal():
    clear_frame()
    tk.Button(frame_matrices, text="Matrices 2x2", command=matrices_2x2).grid(row=0, column=0)
    tk.Button(frame_matrices, text="Matrices 3x3", command=matrices_3x3).grid(row=0, column=1)
    tk.Button(frame_matrices, text="Probabilidades", command=calcular_probabilidades).grid(row=1, column=0)
    tk.Button(frame_matrices, text="Sumas de Riemann", command=sumas_riemann).grid(row=1, column=1)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear un frame para las matrices
frame_matrices = tk.Frame(ventana)
frame_matrices.pack()

menu_principal()

ventana.mainloop()
