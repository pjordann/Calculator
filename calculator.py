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

# con los parámetros, creamos el botón
def crearBoton(texto, numero, ancho, tipoFuente, tamaño_fuente, colorTexto, fila, columna):
    # si quitamos el lambda, automáticamente llamaría a la función de primeras,
    # sin necesidad de darle al 1
    boton = tk.Button(gui, text=texto, command=lambda: calculadora.expresion_anyadir(numero), 
    width=ancho, font=(tipoFuente, tamaño_fuente), foreground=colorTexto, highlightbackground=color)
    
    boton.grid(row=fila, column=columna)

    return boton


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

# creamos botón 1..9
crearBoton("1",1,7,"Arial",14,"#ffffff",2,1)
crearBoton("2",2,7,"Arial",14,"#ffffff",2,2)
crearBoton("3",3,7,"Arial",14,"#ffffff",2,3)
crearBoton("4",4,7,"Arial",14,"#ffffff",3,1)
crearBoton("5",5,7,"Arial",14,"#ffffff",3,2)
crearBoton("6",6,7,"Arial",14,"#ffffff",3,3)
crearBoton("7",7,7,"Arial",14,"#ffffff",4,1)
crearBoton("8",8,7,"Arial",14,"#ffffff",4,2)
crearBoton("9",9,7,"Arial",14,"#ffffff",4,3)
# botón cero
crearBoton("0",0,7,"Arial",14,"#ffffff",5,2)
# creamos botón +,-,*,/,(,)
crearBoton("+","+",7,"Arial",14,"#FF945B",2,4)
crearBoton("-","-",7,"Arial",14,"#FF945B",3,4)
crearBoton("*","*",7,"Arial",14,"#FF945B",4,4)
crearBoton("/","/",7,"Arial",14,"#FF945B",5,4)
crearBoton("(","(",7,"Arial",14,"#000000",5,1)
crearBoton(")",")",7,"Arial",14,"#000000",5,3)

# botones de clear e igual
boton_limpiar = tk.Button(gui, text="C", command=lambda: calculadora.limpiar(), width=14, font=("Arial", 14), highlightbackground=color)
boton_limpiar.grid(row=6, column=1, columnspan=2)
boton_igual = tk.Button(gui, text="=", command=lambda: calculadora.evaluar(), width=14, font=("Arial", 14), highlightbackground=color)
boton_igual.grid(row=6, column=3, columnspan=2)

gui.mainloop()