    # se guarda como ".pyw" para que se pueda abrir como ventana

from tkinter import *

raiz=Tk()

raiz.title("Prueba")  #le pone un titulo a la ventana

raiz.resizable(0,0)   #deja redimensionar la ventana a lo largo o ancho segun su valor boleano

raiz.iconbitmap()  # le pone un icono a la ventana

raiz.geometry("680x350")   #define la dimension de la ventana

raiz.config(bg="Gray")   # define el color del "brackground" o sea del fondo

raiz.mainloop()  # este proceso deber ir al ultimo  (bucle que mantiene la vnetana abierta)


