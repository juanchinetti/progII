#Ejercicio 1.2 - Contador Decreciente

#Este programa decrementa un contador cada vez que se presiona el botón "-". El contador empieza en 88.

import tkinter as tk

def decrementar():
    valor = int(contador_var.get())
    contador_var.set(valor - 1)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Contador Decreciente")

# Etiqueta
tk.Label(ventana, text="Contador").pack()

# LineEdit no editable
contador_var = tk.StringVar(value="88")
tk.Entry(ventana, textvariable=contador_var, state="readonly").pack()

# Botón "-"
tk.Button(ventana, text="-", command=decrementar).pack()

ventana.mainloop()