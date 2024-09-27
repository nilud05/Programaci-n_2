from tkinter import *

ventana = Tk()

texto = Label(ventana, text= "Bienvenidos a mi programa")

texto.config(
        fg="white",
        bg= "black",
        padx=20,
        pady=20,
        font=("Consolas", 30)
)
texto.pack(side=TOP)

texto = Label(ventana, text= "Soy Danitzha")
texto.config(
    justify= RIGHT,
    font= ("Arial", 16),
    bg="orange",
    height=5,
    cursor="spider"
)
texto.pack(side=TOP, fill=X, expand= YES)


texto =Label(ventana, text="Basico")
texto.config(
    height=2,
    bg="pink",
    font=("Arial", 16),
    padx=10,
    pady=20,
    cursor= "spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)


texto =Label(ventana, text="Basico")
texto.config(
    height=2,
    bg="red",
    font=("Arial", 16),
    padx=10,
    pady=20,
    cursor= "spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)


texto =Label(ventana, text="Basico")
texto.config(
    height=2,
    bg="yellow",
    font=("Arial", 16),
    padx=10,
    pady=20,
    cursor= "spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)


ventana.mainloop()