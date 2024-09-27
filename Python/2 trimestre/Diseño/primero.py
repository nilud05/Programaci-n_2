from tkinter import *

class Programa:
    def __init__(self):
        self.title = "Apuntes python Lucia"
        self.icon = './Graficos/icon.ico'
        self.icon_alt = "./Graficos/icon.ico"
        self.size = "770x470"
        self.resizable = False

    def cargar(self):
        ventana = Tk()

        ventana.geometry(self.size)

        ventana.title(self.title)

        ventana.iconbitmap(self.icon_alt)

        if self.resizable:
            ventana.resizable(1, 1) #bloquea el tamaño de la ventana y primero es (ancho, altura)
        else:
            ventana.resizable(0, 0)

        def addTexto():
            texto = Label(ventana, text="Bienvenidos")
            texto=Pack
        
        def mostrar(self):
            self.ventana.mainloop()

programas = Programa()
programas.cargar()