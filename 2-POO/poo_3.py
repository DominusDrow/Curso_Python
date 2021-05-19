#añadimos ejemplo de encapsulamiento de una clase

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


	def __comprobando(self):		#asi es como se encapsula un metodo

		gasolina=True
		puertas=True
		aceite=True

		print("Realizando la comprobacion\n")


		if(gasolina and puertas and aceite):

			return True

		else:

			return False



print("-------------------objeto 1------------------")

coche_1=coche()

print(coche_1.arrancar(True))					#con el encapsulamiento se se puede aceder a variables desde fuera del metodo

coche_1.estado()
																					
print("-------------------objeto 2------------------")

coche_2=coche()

print(coche_1.arrancar(False))

coche_1.estado()







