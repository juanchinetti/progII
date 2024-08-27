import tkinter as tk

def incrementar():
    valor = int(contador_var.get())
    contador_var.set(valor + 1)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Contador Creciente")

# Etiqueta
tk.Label(ventana, text="Contador").pack()

# LineEdit no editable
contador_var = tk.StringVar(value="0")
tk.Entry(ventana, textvariable=contador_var, state="readonly").pack()

# Botón "+"
tk.Button(ventana, text="+", command=incrementar).pack()

ventana.mainloop()