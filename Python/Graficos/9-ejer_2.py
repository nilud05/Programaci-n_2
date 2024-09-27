from tkinter import*
from  tkinter import messagebox

class Calculadora:

    def __init__(self, alertas):
            self.numero1 = StringVar()
            self.numero2 = StringVar()
            self.resultado = StringVar()
            self.alertas = alertas



    def conFloat(self, numero):
        try:
            result = float(numero)
        except:
            result= 0
            messagebox.showerror("Error", "Introduce bien los datos")

        return result

    def sumar(self):
        self.resultado.set(self.conFloat(self.numero1.get()) + self.conFloat(self.numero2.get()))
        self.mostrarResultado()


    def restar(self):
        self.resultado.set(self.conFloat(self.numero1.get()) - self.conFloat(self.numero2.get()))
        self.mostrarResultado()


    def multi(self):
        self.resultado.set(self.conFloat(self.numero1.get()) * self.conFloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.conFloat(self.numero1.get()) / self.conFloat(self.numero2.get()))
        self.mostrarResultado()


    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado de la operación es {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")


ventana = Tk()
ventana.title("Ejercicio completo con Tkinter | Danitzha Payares")
ventana.geometry("400x400")
ventana.config(bd = 25)

calculadora = Calculadora(messagebox)

marco = Frame(ventana, width=250, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)


#Primer numero
Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=Calculadora.numero1, justify="center").pack()

#Segundo numero
Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=Calculadora.numero2, justify="center").pack()

#botones
Button(marco, text="Sumar", command=Calculadora.sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar", command=Calculadora.restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar", command=Calculadora.multi).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Dividir", command=Calculadora.dividir).pack(side=LEFT, fill=X, expand=YES)



ventana.mainloop()