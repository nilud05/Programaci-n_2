from tkinter import *

ventana = Tk()
ventana.geometry("700x500")


texto = Label(ventana, text= "Bienvenidos a mi programa")

texto.config(
        fg="white",
        bg= "black",
        padx=20,
        pady=20,
        font=("Consolas", 30)
)
texto.pack()

texto = Label(ventana, text= "Soy Danitzha")
texto.config(
    justify= RIGHT,
    font= ("Arial", 16),
    bg="orange",
    height=5,
    cursor="spider"
)
texto.pack( anchor=SE)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto =Label(ventana, text= pruebas(nombre="Danitzha", apellidos="Payares", pais="Colombia"))
texto.config(
    height=3,
    bg="red",
    font=("Arial", 16),
    padx=10,
    pady=20,
    cursor= "spider"
)
texto.pack(anchor=NW)


ventana.mainloop()