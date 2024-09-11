#Ejercicio 1.2 - Contador Decreciente



import tkinter as tk

def decrementar():
    valor = int(contador_var.get())
    contador_var.set(valor - 1)


ventana = tk.Tk()
ventana.title("Contador Decreciente")


tk.Label(ventana, text="Contador").pack()


contador_var = tk.StringVar(value="100")
tk.Entry(ventana, textvariable=contador_var, state="readonly").pack()


tk.Button(ventana, text="-", command=decrementar).pack()

ventana.mainloop()