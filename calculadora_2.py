from tkinter import *
from tkinter import messagebox

class Pycalc(Frame):
    def __init__(self, master, *args, **kwargs):
        # Inicializa el marco y configura el widget principal
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()

    def deleteLastCharacter(self):
        # Elimina el último carácter de la entrada
        textLength = len(self.display.get())
        if textLength >= 1:
            self.display.delete(textLength - 1, END)
        if textLength == 1:
            self.replaceText("0")

    def replaceText(self, text):
        # Reemplaza el texto en la entrada
        self.display.delete(0, END)
        self.display.insert(0, text)

    def append(self, text):
        # Añade texto a la entrada
        actualText = self.display.get()
        if actualText == "0":
            self.replaceText(text)
        else:
            self.display.insert(END, text)

    def evaluate(self):
        # Evalúa la expresión matemática y maneja errores
        try:
            result = eval(self.display.get())
            self.replaceText(str(result))
        except SyntaxError:
            messagebox.showerror("Error", "Syntax Error")
            self.replaceText("0")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot Divide by 0")
            self.replaceText("0")

    def containsSigns(self):
        # Verifica si la entrada contiene operadores
        operatorList = ["*", "/", "+", "-"]
        display = self.display.get()
        return any(c in operatorList for c in display)

    def changeSign(self):
        # Cambia el signo del número en la entrada
        if self.containsSigns():
            self.evaluate()
        firstChar = self.display.get()[0]
        if firstChar == "0":
            pass
        elif firstChar == "-":
            self.display.delete(0)
        else:
            self.display.insert(0, "-")

    def inverse(self):
        # Cambia la entrada a su inverso
        self.display.insert(0, "1/(")
        self.append(")")
        self.evaluate()

    def createWidgets(self):
        # Crea y organiza los widgets de la calculadora
        self.display = Entry(self, font=("Arial", 24),
                             relief=RAISED, justify=RIGHT, bg='darkblue', fg='red',
                             borderwidth=0)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Botones de la calculadora
        self.ceButton = Button(self, font=("Arial", 12), fg='red',
                               text="CE", highlightbackground='red', command=lambda: self.replaceText("0"))
        self.ceButton.grid(row=1, column=0, sticky="nsew")

        self.inverseButton = Button(self, font=("Arial", 12),
                                    fg='red', text="1/x", highlightbackground='lightgrey',
                                    command=lambda: self.inverse())
        self.inverseButton.grid(row=1, column=2, sticky="nsew")

        self.delButton = Button(self, font=("Arial", 12),
                                fg='#e8e8e8', text="Del", highlightbackground='red',
                                command=lambda: self.deleteLastCharacter())
        self.delButton.grid(row=1, column=1, sticky="nsew")

        self.divButton = Button(self, font=("Arial", 12), fg='red',
                                text="/", highlightbackground='lightgrey', command=lambda: self.append("/"))
        self.divButton.grid(row=1, column=3, sticky="nsew")

        self.sevenButton = Button(self, font=("Arial", 12),
                                  fg='white', text="7", highlightbackground='black', command=lambda: self.append("7"))
        self.sevenButton.grid(row=2, column=0, sticky="nsew")

        self.eightButton = Button(self, font=("Arial", 12),
                                  fg='white', text="8", highlightbackground='black', command=lambda: self.append("8"))
        self.eightButton.grid(row=2, column=1, sticky="nsew")

        self.nineButton = Button(self, font=("Arial", 12),
                                 fg='white', text="9", highlightbackground='black', command=lambda: self.append("9"))
        self.nineButton.grid(row=2, column=2, sticky="nsew")

        self.multButton = Button(self, font=("Arial", 12),
                                 fg='red', text="*", highlightbackground='lightgrey', command=lambda: self.append("*"))
        self.multButton.grid(row=2, column=3, sticky="nsew")

        self.fourButton = Button(self, font=("Arial", 12),
                                 fg='white', text="4", highlightbackground='black', command=lambda: self.append("4"))
        self.fourButton.grid(row=3, column=0, sticky="nsew")

        self.fiveButton = Button(self, font=("Arial", 12),
                                 fg='white', text="5", highlightbackground='black', command=lambda: self.append("5"))
        self.fiveButton.grid(row=3, column=1, sticky="nsew")

        self.sixButton = Button(self, font=("Arial", 12),
                                fg='white', text="6", highlightbackground='black', command=lambda: self.append("6"))
        self.sixButton.grid(row=3, column=2, sticky="nsew")

        self.minusButton = Button(self, font=("Arial", 12),
                                  fg='red', text="-", highlightbackground='lightgrey', command=lambda: self.append("-"))
        self.minusButton.grid(row=3, column=3, sticky="nsew")

        self.oneButton = Button(self, font=("Arial", 12),
                                fg='white', text="1", highlightbackground='black', command=lambda: self.append("1"))
        self.oneButton.grid(row=4, column=0, sticky="nsew")

        self.twoButton = Button(self, font=("Arial", 12),
                                fg='white', text="2", highlightbackground='black', command=lambda: self.append("2"))
        self.twoButton.grid(row=4, column=1, sticky="nsew")

        self.threeButton = Button(self, font=("Arial", 12),
                                  fg='white', text="3", highlightbackground='black', command=lambda: self.append("3"))
        self.threeButton.grid(row=4, column=2, sticky="nsew")

        self.plusButton = Button(self, font=("Arial", 12),
                                 fg='red', text="+", highlightbackground='lightgrey', command=lambda: self.append("+"))
        self.plusButton.grid(row=4, column=3, sticky="nsew")

        self.negToggleButton = Button(self, font=("Arial", 12),
                                      fg='red', text="+/-", highlightbackground='lightgrey',
                                      command=lambda: self.changeSign())
        self.negToggleButton.grid(row=5, column=0, sticky="nsew")

        self.zeroButton = Button(self, font=("Arial", 12),
                                 fg='white', text="0", highlightbackground='black', command=lambda: self.append("0"))
        self.zeroButton.grid(row=5, column=1, sticky="nsew")

        self.decimalButton = Button(self, font=("Arial", 12),
                                    fg='white', text=".", highlightbackground='lightgrey',
                                    command=lambda: self.append("."))
        self.decimalButton.grid(row=5, column=2, sticky="nsew")

        self.equalsButton = Button(self, font=("Arial", 12),
                                   fg='red', text="=", highlightbackground='lightgrey',
                                   command=lambda: self.evaluate())
        self.equalsButton.grid(row=5, column=3, sticky="nsew")

# Crear la ventana principal y ejecutar la calculadora
if __name__ == "__main__":
    Calculator = Tk()
    Calculator.title("AdictoCalculator")
    Calculator.resizable(False, False)
    Calculator.config(cursor="pencil")
    app = Pycalc(Calculator)
    app.grid()
    Calculator.mainloop()
