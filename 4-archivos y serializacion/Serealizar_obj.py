import pickle

class coche():

	def __init__ (self):    #aqui definimos el estado inicial de una clase

		self.__ruedas=4
		self.__ancho=100        #encapsulamos las varianles iniciales
		self.__largo=300
		self.__marcha=False


	def arrancar(self,op):
		
		self.__marcha=op

		if self.__marcha and self.__comprobando():
			return "el coche esta en marcha"

		elif self.__marcha:

			return "Debido a un fallo no se puede dar marcha"

		else:
			return "el coche esta parado"


	def estado(self):
		
		print("ruedas: ",self.__ruedas," ancho: ",self.__ancho," largo: ",self.__largo)



#creacion de objetos

coche1=coche()

coche2=coche()

coche3=coche()


Coches=[coche1,coche2,coche3]    #aqui se meten todos en una lista


#aqui se volca la lista en un archivo
arch=open("CochesObj","wb")

pickle.dump(Coches,arch)

arch.close()


#Aqui se obtienen de nuevo

bin1=open("CochesObj","rb")

Lista_coches=pickle.load(bin1)

bin1.close()


#a continacion se muestran los objetos

for i in Lista_coches:

	print(i.estado())


