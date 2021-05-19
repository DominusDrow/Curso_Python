
from io import open  #importamos el metod open de la libreria "oi" de python

#para crear y escribir un archivo

arch=open("Escribir.txt","w")

print("\nEscribiendo...\n")

arch.write("Hola como estas?\n yo muy bien :b")
arch.write("\nQUe bueno me alegro \n si asi es ")

arch.close()

#para leer un archivo

arch2=open("leer.txt","r")

print("Leyendo...\n")

lista=arch2.read()

arch2.close()

print(lista)


#para agregar a un archivo

arch3=open("Escribir.txt","a")

print("\nAgregando...\n")

arch3.write("\n  Y esto es un agregado :v")

arch2.close()

