import tkinter as tk
from tkinter import Button, Tk, Frame,Entry,END
class Peliculas(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.config(bg="orange")
        self.n = 1
        self.initUI()

    def initUI(self):

        self.title("Peliculas")
       
        self.label_p = tk.Label(self, text="Escribe los Titulos de las Peliculas", 
                              font=("Arial", 16, "bold"), fg="black", bg="orange")
        self.label_p.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.label_t = tk.Label(self, text="Peliculas", 
                              font=("Arial", 16, "bold"), fg="black", bg="orange")
        self.label_t.grid(row=1, column=1, padx=15, pady=5, sticky="e")

        self.line_edit = tk.Entry(self,font=("Arial", 14), fg= "orange",bg="black")
        self.line_edit.grid(row=2, column=0, padx=0, pady=50)

        self.button_add = tk.Button(self, text="Añadir",command=self.addMovie, font=("Arial", 12), fg="orange", bg="black")
        self.button_add.grid(row=3, column=0, padx=1, pady=0)

        self.listWidget = tk.Listbox(self, font=("Arial", 12), fg="orange",bg='Black')
        self.listWidget.grid(row=2, column=1, padx=10, pady=5)

    def addMovie(self):
        # Añadir el contenido de lineEdit al listWidget
        movie_title = self.line_edit.get()
        if movie_title:
            self.listWidget.insert(tk.END, movie_title)
            self.line_edit.delete(0, tk.END)

if __name__ == "__main__":
    app = Peliculas()
    app.mainloop()