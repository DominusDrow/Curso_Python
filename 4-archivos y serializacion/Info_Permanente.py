#este programa va guardadno una lista en un fichero exxt

import pickle

class persona():

	def __init__(self,nom,gen,e):

		self.nombre=nom
		self.genero=gen
		self.edad=e

		print("\nSe ha credado una nueva persona llamada {} ".format(self.nombre))


	def __str__(self):									 #el metodo "format" se utiliza para dar formato a una cadena

		return " {} {} {} ".format(self.nombre,self.genero,self.edad)



class lista():

	lista_nombres=[]

	def __init__(self):

		try:

			arch=open("lista_nom","ab+")  # ccon este metodo se van agregando 

			arch.seek(0)

			lista_nombres=pickle.load(arch)

			arch.close()

			print("\nCargando archivos\n")

		except:

			print("\nLa lista esta vacia\n")


	
	def aregar_per(self,p1):

		self.lista_nombres.append(p1)  #regresate a la primarai nmms
		self.guardar()


	def mostrar(self):

		for i in self.lista_nombres:  #ACÄ SIMPRE LLEVA "self.lista nombres" , nmms ACUERDATE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	

			print(i)


	def guardar(self):

		finish=open("lista_nom","wb")   #simpre es "arch = open()" IMPORTANTE !!!!!!!!!

		pickle.dump(self.lista_nombres,finish)      #"dump" es para archivos en binario!!!!!!!!!!!!!!!!!!!!!!!!!!! 

		finish.close()

		print("\nLista Guardada\n")


#aqui empiezan las pruebas

listaP=lista()
listaP.mostrar()

p1=persona("Maria","Femenino",14)
p2=persona("Fernado","Femenino",24)


listaP.aregar_per(p1)
listaP.aregar_per(p2)

print("\nLista: \n")
listaP.mostrar()





