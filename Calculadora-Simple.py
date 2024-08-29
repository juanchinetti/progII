#Ejercicio 2 – Calculadora Simple
#Esta aplicación es una calculadora básica que permite realizar operaciones aritméticas simples.


import tkinter as tk

def calcular(operacion):
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    if operacion == "+":
        resultado_var.set(num1 + num2)
    elif operacion == "-":
        resultado_var.set(num1 - num2)
    elif operacion == "*":
        resultado_var.set(num1 * num2)
    elif operacion == "/":
        resultado_var.set(num1 / num2)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Simple")

# Entrada para el primer número
tk.Label(ventana, text="Número 1").grid(row=0, column=0)
entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=1)

# Entrada para el segundo número
tk.Label(ventana, text="Número 2").grid(row=1, column=0)
entrada2 = tk.Entry(ventana)
entrada2.grid(row=1, column=1)

# Botones de operaciones
tk.Button(ventana, text="+", command=lambda: calcular("+")).grid(row=2, column=0)
tk.Button(ventana, text="-", command=lambda: calcular("-")).grid(row=2, column=1)
tk.Button(ventana, text="", command=lambda: calcular("")).grid(row=3, column=0)
tk.Button(ventana, text="/", command=lambda: calcular("/")).grid(row=3, column=1)

# Resultado
tk.Label(ventana, text="Resultado").grid(row=4, column=0)
resultado_var = tk.StringVar()
tk.Entry(ventana, textvariable=resultado_var, state="readonly").grid(row=4, column=1)

ventana.mainloop()