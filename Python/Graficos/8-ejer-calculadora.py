from tkinter import*
from  tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio completo con Tkinter | Danitzha Payares")
ventana.geometry("400x400")
ventana.config(bd = 25)

def conFloat(numero):
    try:
        result = float(numero)
    except:
        result= 0
        messagebox.showerror("Error", "Introduce bien los datos")

    return result

def sumar():
    resultado.set(conFloat(numero1.get()) + conFloat(numero2.get()))
    mostrarResultado()


def restar():
    resultado.set(conFloat(numero1.get()) - conFloat(numero2.get()))
    mostrarResultado()


def multi():
    resultado.set(conFloat(numero1.get()) * conFloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(conFloat(numero1.get()) / conFloat(numero2.get()))
    mostrarResultado()


def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operación es {mostrarResultado.get()}")
    numero1.set("")
    numero2.set("")


numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()


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
Entry(marco, textvariable=numero1).pack()

#Segundo numero
Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=numero2).pack()

#botones
Button(marco, text="Sumar", command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multi).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side=LEFT, fill=X, expand=YES)



ventana.mainloop()