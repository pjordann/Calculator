import tkinter as tk

class Calculadora:
    def __init__(self, input_expresion):
        self.expresion = ""
        self.input_exp = input_expresion
    
    # llamada cada vez que se pulse un símbolo (menos el igual)
    def expresion_anyadir(self, simbolo): 
        self.expresion += str(simbolo)
        # eliminamos todo el contenido de la expresión introducida
        self.input_exp.delete(1.0,"end")     # 1.0: inicio del input. "end": el final
        self.input_exp.insert(1.0, self.expresion)    # introducimos la expresion acumulada

    # llamada cada vez que se pulse el símbolo igual
    def evaluar(self):
        try:
            resultado = str(eval(self.expresion))    # evaluamos la expresión
            self.__setattr__(self.expresion,"")     # volvemos a incializar la expresion
            self.input_exp.delete(1.0, "end")    # borramos todo
            self.input_exp.insert(1.0, resultado)    # insertamos el resultado
        except:
            # en caso de una expresion no válida...
            self.limpiar()
            self.input_exp.insert(1.0, "Error")

    def limpiar(self):
        self.expresion = ""
        self.input_exp.delete(1.0, "end")


gui = tk.Tk()
gui.geometry("240x180")     # tamaño ventana
color = '#0D0D0D'
gui['background']=color
gui.resizable(0,0)          # impide resizear la ventana
gui.title("Calculator")

# tamaño del input, de la caja de texto donde se escribe la expresión a calcular
input_expresion = tk.Text(gui, height=2, width=16, font=("Arial", 24), bg=color, fg="#FFFFFF", highlightbackground=color)
input_expresion.grid(columnspan=5)   # cinco columnas


calculadora = Calculadora(input_expresion)
# si quitamos el lambda, automáticamente llamaría a la función de primeras,
# sin necesidad de darle al 1

boton1 = tk.Button(gui, text="1", command=lambda: calculadora.expresion_anyadir(1), width=7, font=("Arial", 14), foreground="#ffffff", highlightbackground=color)
boton1.grid(row=2, column=1)
boton2 = tk.Button(gui, text="2", command=lambda: calculadora.expresion_anyadir(2), width=7, font=("Arial", 14), foreground="#ffffff", highlightbackground=color)
boton2.grid(row=2, column=2)
boton3 = tk.Button(gui, text="3", command=lambda: calculadora.expresion_anyadir(3), width=7, font=("Arial", 14), foreground="#ffffff", highlightbackground=color)
boton3.grid(row=2, column=3)

boton4 = tk.Button(gui, text="4", command=lambda: calculadora.expresion_anyadir(4), width=7, font=("Arial", 14), foreground="#ffffff", highlightbackground=color)
boton4.grid(row=3, column=1)
boton5 = tk.Button(gui, text="5", command=lambda: calculadora.expresion_anyadir(5), width=7, font=("Arial", 14), foreground="#ffffff", highlightbackground=color)
boton5.grid(row=3, column=2)
boton6 = tk.Button(gui, text="6", command=lambda: calculadora.expresion_anyadir(6), width=7, font=("Arial", 14), foreground="#ffffff", highlightbackground=color)
boton6.grid(row=3, column=3)

boton7 = tk.Button(gui, text="7", command=lambda: calculadora.expresion_anyadir(7), width=7, font=("Arial", 14), foreground="#ffffff", highlightbackground=color)
boton7.grid(row=4, column=1)
boton8 = tk.Button(gui, text="8", command=lambda: calculadora.expresion_anyadir(8), width=7, font=("Arial", 14), foreground="#ffffff", highlightbackground=color)
boton8.grid(row=4, column=2)
boton9 = tk.Button(gui, text="9", command=lambda: calculadora.expresion_anyadir(9), width=7, font=("Arial", 14), foreground="#ffffff", highlightbackground=color)
boton9.grid(row=4, column=3)

boton0 = tk.Button(gui, text="0", command=lambda: calculadora.expresion_anyadir(0), width=7, font=("Arial", 14), foreground="#ffffff", highlightbackground=color)
boton0.grid(row=5, column=2)

botonmas = tk.Button(gui, text="+", command=lambda: calculadora.expresion_anyadir("+"), width=7, font=("Arial", 14), highlightbackground=color)
botonmas.grid(row=2, column=4)
botonmenos = tk.Button(gui, text="-", command=lambda: calculadora.expresion_anyadir("-"), width=7, font=("Arial", 14), highlightbackground=color)
botonmenos.grid(row=3, column=4)
botonmult = tk.Button(gui, text="*", command=lambda: calculadora.expresion_anyadir("*"), width=7, font=("Arial", 14), highlightbackground=color)
botonmult.grid(row=4, column=4)
botondiv = tk.Button(gui, text="/", command=lambda: calculadora.expresion_anyadir("/"), width=7, font=("Arial", 14), highlightbackground=color)
botondiv.grid(row=5, column=4)

boton_abrir_parentesis = tk.Button(gui, text="(", command=lambda: calculadora.expresion_anyadir("("), width=7, font=("Arial", 14), highlightbackground=color)
boton_abrir_parentesis.grid(row=5, column=1)
boton_cerrar_parentesis = tk.Button(gui, text=")", command=lambda: calculadora.expresion_anyadir(")"), width=7, font=("Arial", 14), highlightbackground=color)
boton_cerrar_parentesis.grid(row=5, column=3)

boton_limpiar = tk.Button(gui, text="C", command=lambda: calculadora.limpiar(), width=14, font=("Arial", 14), highlightbackground=color)
boton_limpiar.grid(row=6, column=1, columnspan=2)
boton_igual = tk.Button(gui, text="=", command=lambda: calculadora.evaluar(), width=14, font=("Arial", 14), highlightbackground=color)
boton_igual.grid(row=6, column=3, columnspan=2)

gui.mainloop()