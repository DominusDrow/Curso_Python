#aqui pondremos en pracica el concepto de polimorfismo

class bocho():

	def __init__(self):

		self.__ruedas=4


	def movimiento(self):

		print("Me muevo en: ",self.__ruedas, " ruedas")



class moto():

	def __init__(self):

		self.__ruedas=2


	def movimiento(self):

		print("Me muevo en: ",self.__ruedas, " ruedas")



class Trailer():

	def __init__(self):

		self.__ruedas=8


	def movimiento(self):

		print("Me muevo en: ",self.__ruedas, " ruedas")



def corre(Vehiculo):

	Vehiculo.movimiento()  #en esta funcion aplicamos el polimorfismo



print("\n********bocho********\n")
Vehiculo1=bocho()
corre(Vehiculo1)

print("\n********moto********\n")
Vehiculo2=moto()
corre(Vehiculo2)
