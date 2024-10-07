import tkinter as tk
from tkinter import ttk
from scipy.stats import binom, norm, hypergeom, poisson, geom

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Probabilidades")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Cambia los colores aquí
        self.fondo = "#E67300"  # Color de fondo
        self.color_label = "black"  # Color de texto de las etiquetas
        self.color_button = "black"  # Color de los botones

        # Crear un estilo
        self.style = ttk.Style()
        self.style.configure('TFrame', background=self.fondo)
        self.style.configure('TLabel', background=self.fondo, foreground=self.color_label)
        self.style.configure('TButton', background=self.color_button, foreground=self.color_label)

        self.frame_menu = ttk.Frame(self.root)
        self.frame_menu.pack(pady=10)

        self.label_titulo = ttk.Label(self.frame_menu, text="Seleccione el cálculo que desea realizar", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.button_binomial = ttk.Button(self.frame_menu, text="Binomial", command=self.mostrar_binomial)
        self.button_binomial.pack(pady=5)

        self.button_normal = ttk.Button(self.frame_menu, text="Normal", command=self.mostrar_normal)
        self.button_normal.pack(pady=5)

        self.button_hipergeometrica = ttk.Button(self.frame_menu, text="Hipergeométrica", command=self.mostrar_hipergeometrica)
        self.button_hipergeometrica.pack(pady=5)

        self.button_poisson = ttk.Button(self.frame_menu, text="Poisson", command=self.mostrar_poisson)
        self.button_poisson.pack(pady=5)

        self.button_geometrica = ttk.Button(self.frame_menu, text="Geometría", command=self.mostrar_geometrica)
        self.button_geometrica.pack(pady=5)

        # Frames para cálculos
        self.frame_binomial = self.crear_frame_binomial()
        self.frame_normal = self.crear_frame_normal()
        self.frame_hipergeometrica = self.crear_frame_hipergeometrica()
        self.frame_poisson = self.crear_frame_poisson()
        self.frame_geometrica = self.crear_frame_geometrica()

        # Establecer colores de fondo y texto
        self.establecer_colores()

    def establecer_colores(self):
        # Colocar el fondo en el frame principal
        self.root.configure(bg=self.fondo)

    def crear_frame_binomial(self):
        frame = ttk.Frame(self.root)

        ttk.Label(frame, text="Ingrese n:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_n_binomial = ttk.Entry(frame)
        self.entry_n_binomial.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ingrese p:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_p_binomial = ttk.Entry(frame)
        self.entry_p_binomial.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ingrese x:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_x_binomial = ttk.Entry(frame)
        self.entry_x_binomial.grid(row=2, column=1, padx=5, pady=5)

        self.label_resultado_binomial = ttk.Label(frame, text="")
        self.label_resultado_binomial.grid(row=4, columnspan=2, pady=5)

        button_calcular = ttk.Button(frame, text="Calcular Binomial", command=self.calcular_binomial)
        button_calcular.grid(row=3, columnspan=2, pady=5)

        button_limpiar = ttk.Button(frame, text="Limpiar Campos", command=self.limpiar_campos_binomial)
        button_limpiar.grid(row=5, columnspan=2, pady=5)

        return frame

    def crear_frame_normal(self):
        frame = ttk.Frame(self.root)

        ttk.Label(frame, text="Ingrese media (μ):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_media_normal = ttk.Entry(frame)
        self.entry_media_normal.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ingrese desviación estándar (σ):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_desviacion_normal = ttk.Entry(frame)
        self.entry_desviacion_normal.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ingrese valor inferior (x1):").grid(row=2, column=0, padx=5, pady=5)
        self.entry_x_inferior_normal = ttk.Entry(frame)
        self.entry_x_inferior_normal.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ingrese valor superior (x2):").grid(row=3, column=0, padx=5, pady=5)
        self.entry_x_superior_normal = ttk.Entry(frame)
        self.entry_x_superior_normal.grid(row=3, column=1, padx=5, pady=5)

        self.label_resultado_normal = ttk.Label(frame, text="")
        self.label_resultado_normal.grid(row=5, columnspan=2, pady=5)

        button_calcular = ttk.Button(frame, text="Calcular Normal", command=self.calcular_normal)
        button_calcular.grid(row=4, columnspan=2, pady=5)

        button_limpiar = ttk.Button(frame, text="Limpiar Campos", command=self.limpiar_campos_normal)
        button_limpiar.grid(row=6, columnspan=2, pady=5)

        return frame

    def crear_frame_hipergeometrica(self):
        frame = ttk.Frame(self.root)

        ttk.Label(frame, text="Ingrese N:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_N_hipergeometrica = ttk.Entry(frame)
        self.entry_N_hipergeometrica.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ingrese K:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_K_hipergeometrica = ttk.Entry(frame)
        self.entry_K_hipergeometrica.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ingrese n:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_n_hipergeometrica = ttk.Entry(frame)
        self.entry_n_hipergeometrica.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ingrese k:").grid(row=3, column=0, padx=5, pady=5)
        self.entry_k_hipergeometrica = ttk.Entry(frame)
        self.entry_k_hipergeometrica.grid(row=3, column=1, padx=5, pady=5)

        self.label_resultado_hipergeometrica = ttk.Label(frame, text="")
        self.label_resultado_hipergeometrica.grid(row=5, columnspan=2, pady=5)

        button_calcular = ttk.Button(frame, text="Calcular Hipergeométrica", command=self.calcular_hipergeometrica)
        button_calcular.grid(row=4, columnspan=2, pady=5)

        button_limpiar = ttk.Button(frame, text="Limpiar Campos", command=self.limpiar_campos_hipergeometrica)
        button_limpiar.grid(row=6, columnspan=2, pady=5)

        return frame

    def crear_frame_poisson(self):
        frame = ttk.Frame(self.root)

        ttk.Label(frame, text="Ingrese λ (media):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_lambda_poisson = ttk.Entry(frame)
        self.entry_lambda_poisson.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ingrese k (número de eventos):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_k_poisson = ttk.Entry(frame)
        self.entry_k_poisson.grid(row=1, column=1, padx=5, pady=5)

        self.label_resultado_poisson = ttk.Label(frame, text="")
        self.label_resultado_poisson.grid(row=3, columnspan=2, pady=5)

        button_calcular = ttk.Button(frame, text="Calcular Poisson", command=self.calcular_poisson)
        button_calcular.grid(row=2, columnspan=2, pady=5)

        button_limpiar = ttk.Button(frame, text="Limpiar Campos", command=self.limpiar_campos_poisson)
        button_limpiar.grid(row=4, columnspan=2, pady=5)

        return frame

    def crear_frame_geometrica(self):
        frame = ttk.Frame(self.root)

        ttk.Label(frame, text="Ingrese p (probabilidad de éxito):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_p_geometrica = ttk.Entry(frame)
        self.entry_p_geometrica.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Ingrese k (número de intentos):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_k_geometrica = ttk.Entry(frame)
        self.entry_k_geometrica.grid(row=1, column=1, padx=5, pady=5)

        self.label_resultado_geometrica = ttk.Label(frame, text="")
        self.label_resultado_geometrica.grid(row=3, columnspan=2, pady=5)

        button_calcular = ttk.Button(frame, text="Calcular Geometría", command=self.calcular_geometrica)
        button_calcular.grid(row=2, columnspan=2, pady=5)

        button_limpiar = ttk.Button(frame, text="Limpiar Campos", command=self.limpiar_campos_geometrica)
        button_limpiar.grid(row=4, columnspan=2, pady=5)

        return frame

    def mostrar_binomial(self):
        self.ocultar_frames()
        self.frame_binomial.pack()

    def mostrar_normal(self):
        self.ocultar_frames()
        self.frame_normal.pack()

    def mostrar_hipergeometrica(self):
        self.ocultar_frames()
        self.frame_hipergeometrica.pack()

    def mostrar_poisson(self):
        self.ocultar_frames()
        self.frame_poisson.pack()

    def mostrar_geometrica(self):
        self.ocultar_frames()
        self.frame_geometrica.pack()

    def ocultar_frames(self):
        self.frame_binomial.pack_forget()
        self.frame_normal.pack_forget()
        self.frame_hipergeometrica.pack_forget()
        self.frame_poisson.pack_forget()
        self.frame_geometrica.pack_forget()

    def calcular_binomial(self):
        try:
            n = int(self.entry_n_binomial.get())
            p = float(self.entry_p_binomial.get())
            x = int(self.entry_x_binomial.get())
            resultado = binom.pmf(x, n, p)
            self.label_resultado_binomial.config(text=f"Probabilidad: {resultado:.4f}")
        except ValueError:
            self.label_resultado_binomial.config(text="Por favor, ingrese valores válidos.")

    def limpiar_campos_binomial(self):
        self.entry_n_binomial.delete(0, tk.END)
        self.entry_p_binomial.delete(0, tk.END)
        self.entry_x_binomial.delete(0, tk.END)
        self.label_resultado_binomial.config(text="")

    def calcular_normal(self):
        try:
            media = float(self.entry_media_normal.get())
            desviacion = float(self.entry_desviacion_normal.get())
            x_inferior = self.entry_x_inferior_normal.get()
            x_superior = self.entry_x_superior_normal.get()

            if x_inferior and x_superior:
                x1 = float(x_inferior)
                x2 = float(x_superior)
                resultado = norm.cdf(x2, media, desviacion) - norm.cdf(x1, media, desviacion)
                self.label_resultado_normal.config(text=f"Probabilidad entre {x1} y {x2}: {resultado:.4f}")
            elif x_inferior:  # Solo el límite inferior
                x1 = float(x_inferior)
                resultado = 1 - norm.cdf(x1, media, desviacion)
                self.label_resultado_normal.config(text=f"Probabilidad de más de {x1}: {resultado:.4f}")
            elif x_superior:  # Solo el límite superior
                x2 = float(x_superior)
                resultado = norm.cdf(x2, media, desviacion)
                self.label_resultado_normal.config(text=f"Probabilidad de hasta {x2}: {resultado:.4f}")
            else:
                self.label_resultado_normal.config(text="Por favor, ingrese al menos un límite.")
        except ValueError:
            self.label_resultado_normal.config(text="Por favor, ingrese valores válidos.")

    def limpiar_campos_normal(self):
        self.entry_media_normal.delete(0, tk.END)
        self.entry_desviacion_normal.delete(0, tk.END)
        self.entry_x_inferior_normal.delete(0, tk.END)
        self.entry_x_superior_normal.delete(0, tk.END)
        self.label_resultado_normal.config(text="")

    def calcular_hipergeometrica(self):
        try:
            N = int(self.entry_N_hipergeometrica.get())
            K = int(self.entry_K_hipergeometrica.get())
            n = int(self.entry_n_hipergeometrica.get())
            k = int(self.entry_k_hipergeometrica.get())
            resultado = hypergeom.pmf(k, N, K, n)
            self.label_resultado_hipergeometrica.config(text=f"Probabilidad: {resultado:.4f}")
        except ValueError:
            self.label_resultado_hipergeometrica.config(text="Por favor, ingrese valores válidos.")

    def limpiar_campos_hipergeometrica(self):
        self.entry_N_hipergeometrica.delete(0, tk.END)
        self.entry_K_hipergeometrica.delete(0, tk.END)
        self.entry_n_hipergeometrica.delete(0, tk.END)
        self.entry_k_hipergeometrica.delete(0, tk.END)
        self.label_resultado_hipergeometrica.config(text="")

    def calcular_poisson(self):
        try:
            lam = float(self.entry_lambda_poisson.get())
            k = int(self.entry_k_poisson.get())
            resultado = poisson.pmf(k, lam)
            self.label_resultado_poisson.config(text=f"Probabilidad: {resultado:.4f}")
        except ValueError:
            self.label_resultado_poisson.config(text="Por favor, ingrese valores válidos.")

    def limpiar_campos_poisson(self):
        self.entry_lambda_poisson.delete(0, tk.END)
        self.entry_k_poisson.delete(0, tk.END)
        self.label_resultado_poisson.config(text="")

    def calcular_geometrica(self):
        try:
            p = float(self.entry_p_geometrica.get())
            k = int(self.entry_k_geometrica.get())
            resultado = geom.pmf(k, p)
            self.label_resultado_geometrica.config(text=f"Probabilidad: {resultado:.4f}")
        except ValueError:
            self.label_resultado_geometrica.config(text="Por favor, ingrese valores válidos.")

    def limpiar_campos_geometrica(self):
        self.entry_p_geometrica.delete(0, tk.END)
        self.entry_k_geometrica.delete(0, tk.END)
        self.label_resultado_geometrica.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()