#primer programa con el paradigma orientado a objetos

class coche():

	ruedas=4
	largo=200
	ancho=100
	movimiento=False


	def arrancar(self):
		
		self.movimiento=True


	def comprobar_mov(self):
		
		if self.movimiento==True:

			return "El coche esta en movimiento"

		else:

			return "El coche no esta en movimeinto"


coche_1=coche()

print("el coche tiene",coche_1.ruedas,"ruedas")
print("el coche tiene un ancho de",coche_1.ancho)

print(coche_1.comprobar_mov())

coche_1.arrancar()

print(coche_1.comprobar_mov())

