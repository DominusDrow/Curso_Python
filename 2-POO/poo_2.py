#aqui pondremos a prueba el concepto de encasulamiento y estado inicial

class coche():

	def __init__(self): #asi se define un estado inical de una clase

		self.__ruedas=4
		self.__ancho=100
		self.__largo=300	#con los dos guines (__) se encapsula la variable
		self.__mov=False


	def arrancar(self,est):

		self.__mov=est

		if self.__mov:
			return "esta en movimiento"

		else:
			return "no esta en movimiento"


	def estado(self):

		print("ruedas: ",self.__ruedas," ancho: ",self.__ancho," largo: ",self.__largo)
	


print("-------------------objeto 1------------------")

coche_1=coche()

print(coche_1.arrancar(True))

coche_1.estado()
																					
print("-------------------objeto 2------------------")

coche_2=coche()

print(coche_1.arrancar(False))

coche_1.estado()


	

