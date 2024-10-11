import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import re

# Validar si la contraseña cumple con los requisitos
def validar_contraseña(password):
    if len(password) < 6:  #longitud
        return False
    if not re.search(r'[A-Z]', password): #una mayúscula
        return False
    if not re.search(r'[a-z]', password): #una minúscula
        return False
    if not re.search(r'[0-9]', password): #un número
        return False
    return True

# Validar el inicio de sesión
def login():
    username = entry_username.get()
    password = entry_password.get()

    #Validación de usuario y contraseña
    if username == "admin" and validar_contraseña(password):
        messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
    else:
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos. \n"
                                      "La contraseña debe tener al menos una mayúscula, una minúscula y un número.")

#Ventana principal
root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("800x600")  #Tamaño de ventana

#Color de fondo de la ventana
root.config(bg="#FFA500")

#Cargar y redimensionar la imagen del logo
logo_path = "D:/Usuario/Pictures/imagenes de trabajo/Logo_Handball_(2).png"
image = Image.open(logo_path)  
image = image.resize((300, 200), Image.LANCZOS)  
logo = ImageTk.PhotoImage(image)

#el logo en la ventana
logo_label = tk.Label(root, image=logo, bg="#FFA500")
logo_label.pack(pady=5)  #para justar el espacio alrededor de la imagen

# Título de la interfazdos
label_title = tk.Label(root, text="Inicio de Sesión", font=("Arial", 18, "bold"), bg="#FFA500", fg="black")
label_title.pack(pady=10)  #Espacio superior e inferior del título

#Nombre de usuario
label_username = tk.Label(root, text="Nombre de Usuario:", bg="#FFA500", fg="#000000", font=("Arial", 14, "bold"))
label_username.pack(pady=5)
entry_username = tk.Entry(root, font=("Arial", 12))
entry_username.pack(pady=5, ipadx=20, ipady=5)

#Contraseña
label_password = tk.Label(root, text="Contraseña:", bg="#FFA500", fg="#000000", font=("Arial", 14, "bold"))
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*", font=("Arial", 12))
entry_password.pack(pady=5, ipadx=20, ipady=5)

#Botón de iniciar sesión
button_login = tk.Button(root, text="Iniciar Sesión", command=login, bg="#FFFFFF", fg="#000000", activebackground="#DDDDDD", activeforeground="#000000", font=("Arial", 12, "bold"))
button_login.pack(pady=20)

#Ejecutar la aplicación
root.mainloop()
