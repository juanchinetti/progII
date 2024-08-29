#Ejercicio 1.4 - Contador con Reset
#Este programa tiene tres botones: "Count Up" para incrementar, "Count Down" para decrementar, y "Reset" para poner el contador en cero.

import tkinter as tk

def incrementar():
    valor = int(contador_var.get())
    contador_var.set(valor + 1)

def decrementar():
    valor = int(contador_var.get())
    contador_var.set(valor - 1)

def resetear():
    contador_var.set(0)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Contador")

# Etiqueta
tk.Label(ventana, text="Contador").pack()

# LineEdit no editable
contador_var = tk.StringVar(value="0")
tk.Entry(ventana, textvariable=contador_var, state="readonly").pack()

# Botones
tk.Button(ventana, text="Count Up", command=incrementar).pack()
tk.Button(ventana, text="Count Down", command=decrementar).pack()
tk.Button(ventana, text="Reset", command=resetear).pack()

ventana.mainloop()