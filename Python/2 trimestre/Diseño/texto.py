from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text= "Bienvenidos a mi programa")
texto.pack()
texto.config(
        fg="white",
        bg= "black",
        padx=20,
        pady=20
)