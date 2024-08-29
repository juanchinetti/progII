#Ejercicio 1.3 – Factorial
#Este programa calcula el factorial de un número ingresado en un LineEdit y muestra el resultado en otro LineEdit al presionar "Siguiente".

import tkinter as tk
from math import factorial

def calcular_factorial():
    n = int(valor_n.get())
    resultado_var.set(factorial(n))
    valor_n.set(n + 1)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Factorial")

# Etiquetas y LineEdit no editables
tk.Label(ventana, text="n:").pack()
valor_n = tk.StringVar(value="1")
tk.Entry(ventana, textvariable=valor_n, state="readonly").pack()

tk.Label(ventana, text="Factorial(n):").pack()
resultado_var = tk.StringVar(value="1")
tk.Entry(ventana, textvariable=resultado_var, state="readonly").pack()

# Botón "Siguiente"
tk.Button(ventana, text="Siguiente", command=calcular_factorial).pack()

ventana.mainloop()