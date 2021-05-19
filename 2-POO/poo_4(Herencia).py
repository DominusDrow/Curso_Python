#aqui ponemos en practica el concepto de herencia

class Vehiculos():

	def __init__(self,m,mod): #se define un estdo inicial

		self.marca=m
		self.modelo=mod
		self.__marcha=False	
		self.__acelerar=False		#se encapsulan valiables importantes
		self.__frenar=False


	def arrancar(self):
		self.__marcha=True

	def acelelar(self):
		self.__acelerar=True

	def frenar(self):
		self.__frenar=True

	def estado(self):
		
		print("\nMarca: ",self.marca,"\nModelo: ",self.modelo,"\narrancar: ",self.__marcha,"\nfreno: "
			,self.__frenar,"\nacerelar: ",self.__acelerar)


class V_elictricos(Vehiculos):

	def __init__(self,m,mod):

		super().__init__(m,mod)
		self.__carga=100
		self.__cargando=False


	def estado(self):

		super().estado()
		print("carga: ",self.__carga,"\nCargando: ",self.__cargando)


	def carg(self,est):

		self.__cargando=est


		if self.__cargando:
			return "se esta cargando"

		else:

			return "No se esta cargando"



class moto(Vehiculos):   #Esta clase va a heredar de la clase vehiculos

	__llantas=2
	__manejo="manubrio"
	__trucos=False

	def trucos(self):

		self.__trucos=True

		if self.__trucos:
			print("Esta haciendo trucos")


		else:
			print("No esta haciendo trucos")
	

	def estado(self):          #Abajo sobreescrinimos el metodo "estado", esto solo aplicara en la clase "moto"
		
		Vehiculos.estado(self)  #asi es una forma recortada
		self.trucos()
		print("manejo: ",self.__manejo)




class moto_electrica(V_elictricos,moto):   #esta clase va a heredar de dos clases (Vehiculos y V_electricos)
	
	pass


print("\n**********Vehiculo mecanico**********")
moto_1=moto("zusuki","reygan")
moto_1.estado()


print("\n**********Vehiculo electrico**********")
moto_2=moto_electrica("Honda","reyxen")
moto_2.estado()
print(moto_2.carg(False))


print("\n",isinstance(moto_2,V_elictricos))      #isinstance es para comprobar a que clases pertenece un objeto
