#Ejercicio 3 – Generador de Números Aleatorios
#Este programa genera un número aleatorio dentro de un rango definido por el usuario.

import tkinter as tk
import random

def generar_numero():
    min_valor = int(entrada_min.get())
    max_valor = int(entrada_max.get())
    numero = random.randint(min_valor, max_valor)
    resultado_var.set(numero)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Números Aleatorios")

# Rango mínimo
tk.Label(ventana, text="Mínimo").grid(row=0, column=0)
entrada_min = tk.Entry(ventana)
entrada_min.grid(row=0, column=1)

# Rango máximo
tk.Label(ventana, text="Máximo").grid(row=1, column=0)
entrada_max = tk.Entry(ventana)
entrada_max.grid(row=1, column=1)

# Botón para generar
tk.Button(ventana, text="Generar", command=generar_numero).grid(row=2, columnspan=2)

# Resultado
resultado_var = tk.StringVar()
tk.Entry(ventana, textvariable=resultado_var, state="readonly").grid(row=3, columnspan=2)

ventana.mainloop()