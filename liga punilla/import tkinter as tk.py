import tkinter as tk
from tkinter import messagebox
import re  # Para trabajar con expresiones regulares

# Validar si la contraseña cumple con los requisitos
def validar_contraseña(password):
    if len(password) < 6:  # Mínimo de longitud
        return False
    if not re.search(r'[A-Z]', password):  # Al menos una mayúscula
        return False
    if not re.search(r'[a-z]', password):  # Al menos una minúscula
        return False
    if not re.search(r'[0-9]', password):  # Al menos un número
        return False
    return True

# Validar el inicio de sesión
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Validación de usuario y contraseña
    if username == "admin" and validar_contraseña(password):
        messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
    else:
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos. \n"
                                      "La contraseña debe tener al menos una mayúscula, una minúscula y un número.")

# Ventana principal
root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("800x600")  # Tamaño de la ventana

# Color de fondo naranja
root.config(bg="#FFA500")

# Agregar la imagen del logo (asegúrate de que el archivo esté en la misma carpeta o especifica la ruta)
# logo = tk.PhotoImage(file="/mnt/data/image.png")  # Imagen
# logo_label = tk.Label(root, image=logo, bg="#FFA500")
# logo_label.pack(pady=20)  # Ajusta el padding según tu diseño

# Título de la interfaz con colores personalizados
label_title = tk.Label(root, text="Inicio de Sesión", font=("Arial", 18), bg="#FFA500", fg="#FFFFFF")
label_title.pack(pady=10)

# Nombre de usuario
label_username = tk.Label(root, text="Nombre de Usuario:", bg="#FFA500", fg="#FFFFFF")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Contraseña
label_password = tk.Label(root, text="Contraseña:", bg="#FFA500", fg="#FFFFFF")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Botón de iniciar sesión
button_login = tk.Button(root, text="Iniciar Sesión", command=login, bg="#FFBC42", fg="#FFFFFF", activebackground="#FF9F1C", activeforeground="#FFFFFF")
button_login.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
