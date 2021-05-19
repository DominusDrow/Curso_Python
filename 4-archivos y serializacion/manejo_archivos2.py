# aqui veremos mas formas de manipular un archivo

from io import open

arch=open("Mucho Texto.txt","r+")    #aqui se abre el archivo



print("\n*Cuando se abre el archivo: \n",arch.read()) 


arch.seek(0)
print("\n*Puntero en 0: \n",arch.read())


arch.seek(0)
print("\n*Leer por lineas: \n")

print(arch.readline())      # aqui se usa readline que lee una sola linea
print(arch.readline())

arch.seek(0)     #aqui se reinicia el punturo

arch.seek(len(arch.readline()))

print("\n*Leer la midad del earchivo \n",arch.read())

#aqui escribrimos algo en el texto original

arch.seek(0)
arch.seek(len(arch.read()))

arch.write("\n\nAQUI no comienza el texto xd\n")

arch.seek(0)
print("\n*luego de agregar una linea: \n",arch.read())


# aqui es donde modificamos el mensaje del texto:

arch.seek(0)

lista_texto=arch.readlines()  # aqui se usa readlines que lee todos las lineas

lista_texto[1]="Esto ya no es una prueba een pyhton"

arch.seek(0)
arch.writelines(lista_texto)

arch.seek(0)
print("\n*Luego de cambiar una linea de txt: \n",arch.read())

arch.close() #aqui se cierra el archivo




