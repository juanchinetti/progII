#Ejercicio 1.3 – Factorial


import tkinter as tk
from math import factorial

def calcular_factorial():
    n = int(valor_n.get())
    resultado_var.set(factorial(n))
    valor_n.set(n + 1)


ventana = tk.Tk()
ventana.title("Factorial")

tk.Label(ventana, text="n:").pack()
valor_n = tk.StringVar(value="1")
tk.Entry(ventana, textvariable=valor_n, state="readonly").pack()

tk.Label(ventana, text="Factorial(n):").pack()
resultado_var = tk.StringVar(value="1")
tk.Entry(ventana, textvariable=resultado_var, state="readonly").pack()


tk.Button(ventana, text="Siguiente", command=calcular_factorial).pack()

ventana.mainloop()