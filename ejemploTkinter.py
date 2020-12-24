from tkinter import *

class interfaz:
    def __init__(self, contenedor):
        self.e1 = Label(contenedor, text="Mi ventana", fg="black") 
        self.e1.pack()

ventana = Tk()
minterfaz = interfaz(ventana)
ventana.mainloop()
