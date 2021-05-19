#aplicamos lo que es un frame

from tkinter import *

raiz=Tk()

raiz.title("Frame")

raiz.resizable(0,0)   #deja redimensionar la ventana a lo largo o ancho segun su valor boleano

#raiz.iconbitmap("estrategia.ico")  # le pone un icono a la ventana

raiz.geometry("680x300")   #define la dimension de la ventana

raiz.config(bg="green")   # define el color del "brackground" o sea del fondo



raiz.mainloop()     