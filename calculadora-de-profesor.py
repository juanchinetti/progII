from tkinter import Tk, Button, Frame, Entry, END, messagebox

class HoverButton(Button):
    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    
    def on_enter(self, e):
        self["background"] = self["activebackground"]
    
    def on_leave(self, e):
        self["background"] = self.defaultBackground

class Calculator(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.display = Entry(self, font=("Arial", 24), relief="raised", justify="right", bg='darkblue', fg='red', borderwidth=0)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('CE', 1, 0, self.clear_entry),
            ('1/x', 1, 1, self.inverse),
            ('Del', 1, 2, self.delete_last_character),
            ('/', 1, 3, lambda: self.append('/')),
            ('7', 2, 0, lambda: self.append('7')),
            ('8', 2, 1, lambda: self.append('8')),
            ('9', 2, 2, lambda: self.append('9')),
            ('*', 2, 3, lambda: self.append('*')),
            ('4', 3, 0, lambda: self.append('4')),
            ('5', 3, 1, lambda: self.append('5')),
            ('6', 3, 2, lambda: self.append('6')),
            ('-', 3, 3, lambda: self.append('-')),
            ('1', 4, 0, lambda: self.append('1')),
            ('2', 4, 1, lambda: self.append('2')),
            ('3', 4, 2, lambda: self.append('3')),
            ('+', 4, 3, lambda: self.append('+')),
            ('0', 5, 0, lambda: self.append('0')),
            ('.', 5, 1, lambda: self.append('.')),
            ('=', 5, 2, self.evaluate),
            ('√', 5, 3, lambda: self.append('**(1/2)'))
        ]

        for (text, row, col, command) in buttons:
            button = HoverButton(self, text=text, font=("Arial", 12), height=2, width=5, relief="raised", activebackground="aqua", bg='#999AB8', command=command)
            button.grid(row=row, column=col, pady=2, padx=2, sticky="nsew")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
    
    def clear_entry(self):
        self.display.delete(0, END)
        self.display.insert(0, "0")

    def inverse(self):
        try:
            value = eval(self.display.get())
            self.display.delete(0, END)
            self.display.insert(0, 1 / value)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot Divide by 0")
            self.clear_entry()

    def delete_last_character(self):
        length = len(self.display.get())
        if length > 1:
            self.display.delete(length - 1)
        else:
            self.clear_entry()
    
    def append(self, text):
        current = self.display.get()
        if current == "0":
            self.display.delete(0, END)
        self.display.insert(END, text)

    def evaluate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, END)
            self.display.insert(0, result)
        except (SyntaxError, AttributeError):
            messagebox.showerror("Error", "Syntax Error")
            self.clear_entry()
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot Divide by 0")
            self.clear_entry()

if __name__ == "__main__":
    root = Tk()
    root.title("Calculadora")
    root.geometry('400x400')
    root.resizable(False, False)
    Calculator(root).grid()
    root.mainloop()