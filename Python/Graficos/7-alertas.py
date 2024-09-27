from tkinter import *
from tkinter import messagebox as MessageBox


ventana = Tk()
ventana.config(bd=70)

def sacaralerta():
    MessageBox.showwarning("Alerta", "Hola soy Danitzha Payares")

Button(ventana,text="Mostrar alerta!!!", command=sacaralerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¡Continuar ejecutando la aplicación?")

    if resultado !="yes":
        MessageBox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()

Button(ventana,text="Salir", command=lambda: salir("Danitzha Payares")).pack()


ventana.mainloop()