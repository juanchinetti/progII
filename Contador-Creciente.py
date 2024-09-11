#Ejercicio 1.1 - Contador Creciente


import tkinter as tk

def incrementar():
    valor = int(contador_var.get())
    contador_var.set(valor + 1)


ventana = tk.Tk()
ventana.title("Contador Creciente")


tk.Label(ventana, text="Contador").pack()


contador_var = tk.StringVar(value="0")
tk.Entry(ventana, textvariable=contador_var, state="readonly").pack()


tk.Button(ventana, text="+", command=incrementar).pack()

ventana.mainloop()