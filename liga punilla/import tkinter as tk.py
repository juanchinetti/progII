import tkinter as tk
from tkinter import messagebox

# Función para validar el inicio de sesión
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Lógica de validación (aquí puedes conectarlo a tu base de datos)
    if username == "admin" and password == "1234":
        messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
    else:
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")

# Crear la ventana principal
root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("400x400")  # Ajusta el tamaño según tu diseño

# Establecer color de fondo (usa el color de tu diseño)
root.config(bg="#0C345B")  # Cambia este color por el que necesites

# Agregar la imagen del logo (asegúrate de que el archivo esté en la misma carpeta o especifica la ruta)
logo = tk.PhotoImage(file="/mnt/data/image.png")  # Coloca la ruta correcta de tu imagen
logo_label = tk.Label(root, image=logo, bg="#0C345B")
logo_label.pack(pady=20)  # Ajusta el padding según tu diseño

# Título de la interfaz con colores personalizados
label_title = tk.Label(root, text="Inicio de Sesión", font=("Arial", 18), bg="#0C345B", fg="#FFFFFF")  # Cambia colores si es necesario
label_title.pack(pady=10)

# Campo para el nombre de usuario
label_username = tk.Label(root, text="Nombre de Usuario:", bg="#0C345B", fg="#FFFFFF")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Campo para la contraseña
label_password = tk.Label(root, text="Contraseña:", bg="#0C345B", fg="#FFFFFF")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Botón para iniciar sesión (personaliza los colores del botón)
button_login = tk.Button(root, text="Iniciar Sesión", command=login, bg="#FFBC42", fg="#FFFFFF", activebackground="#FF9F1C", activeforeground="#FFFFFF")
button_login.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
