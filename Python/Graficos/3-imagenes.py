from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola, soy Danitzha!!").pack(anchor=W)

imagen = Image.open('./Graficos/img/atardecer.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()


ventana.mainloop()