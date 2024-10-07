import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# Variables globales para los entries
entry_a1 = entry_b1 = entry_c1 = entry_d1 = None
entry_a2 = entry_b2 = entry_c2 = entry_d2 = None
entry_a3 = entry_b3 = entry_c3 = entry_d3 = None

def gauss_jordan(matrix):
    n = len(matrix)

    # Aplicar el método de Gauss-Jordan
    for i in range(n):
        # Hacer que el elemento diagonal sea 1
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

def mostrar_opciones():
    clear_frame()
    tk.Label(frame_matrices, text="Selecciona la dimensión del sistema:").grid(row=0, column=0, columnspan=2)
    tk.Button(frame_matrices, text="2x2", command=matrices_2x2).grid(row=1, column=0)
    tk.Button(frame_matrices, text="3x3", command=matrices_3x3).grid(row=1, column=1)

def calcular_probabilidades():
    # Aquí puedes añadir tu código de la calculadora de probabilidades.
    messagebox.showinfo("Calculadora de Probabilidades", "Aquí va la calculadora de probabilidades.")

def clear_frame():
    for widget in frame_matrices.winfo_children():
        widget.destroy()

root = tk.Tk()
root.title("Calculadora de Probabilidades y Matrices")

frame_matrices = tk.Frame(root)
frame_matrices.pack(pady=10)

menu = tk.Menu(root)
root.config(menu=menu)

menu_calculos = tk.Menu(menu)
menu.add_cascade(label="Calcular", menu=menu_calculos)
menu_calculos.add_command(label="Matrices", command=mostrar_opciones)
menu_calculos.add_command(label="Probabilidades", command=calcular_probabilidades)

root.mainloop()