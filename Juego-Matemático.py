#Ejercicio 4 – Juego Matemático

import tkinter as tk
import random

def generar_operacion():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operacion = random.choice(["+", "-", "*", "/"])
    
    if operacion == "+":
        resultado_correcto = num1 + num2
    elif operacion == "-":
        resultado_correcto = num1 - num2
    elif operacion == "*":
        resultado_correcto = num1 * num2
    else:  # operacion == "/"
        resultado_correcto = num1 / num2

    operacion_var.set(f"{num1} {operacion} {num2}")
    resultado_esperado_var.set(resultado_correcto)

def verificar_respuesta():
    respuesta_usuario = float(respuesta_var.get())
    resultado_correcto = float(resultado_esperado_var.get())

    if respuesta_usuario == resultado_correcto:
        resultado_var.set("Correcto!")
    else:
        resultado_var.set("Incorrecto!")

    
ventana = tk.Tk()
ventana.title("Juego Matemático")
 

operacion_var = tk.StringVar()
tk.Label(ventana, textvariable=operacion_var).grid(row=0, columnspan=2)


tk.Label(ventana, text="Tu Respuesta:").grid(row=1, column=0)
respuesta_var = tk.Entry(ventana)
respuesta_var.grid(row=1, column=1)


tk.Button(ventana, text="Verificar", command=verificar_respuesta).grid(row=2, columnspan=2)


resultado_var = tk.StringVar()
tk.Label(ventana, textvariable=resultado_var).grid(row=3, columnspan=2)


resultado_esperado_var = tk.StringVar()


generar_operacion()

ventana.mainloop()