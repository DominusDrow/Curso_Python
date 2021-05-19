#aqui veremos como crear un archivo binario

import pickle

 
arch=open("nombres_bin","wb")    #este modo es para binario

lista_nombres=["Jorge","Hector","Luis","Alfonso","Alfredo","Atanasio","I"]

pickle.dump(lista_nombres,arch)


arch.close()


del (lista_nombres)  # el metodo "del" funciona para eliminar info