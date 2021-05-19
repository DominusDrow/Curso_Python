#pondremos en practica el uso del metodo super

class persona():                     

	def __init__(self,nombre,edad,localidad):

		self.nom=nombre 
		self.edad=edad                   #la primera clase es de persona
		self.loc=localidad



	def info(self):

		print("nombre: ",self.nom," edad: ",self.edad," localidad: ",self.loc)



class empleado(persona):

	def __init__(self,sul,anti,nombre,edad,localidad):

		super().__init__(nombre,edad,localidad)       #super llama a la clase padre para poder usar sus metodos

		self.sueldo=sul
		self.antiguedad=anti



	def info_empleado(self):

		super().info()	

		print("sueldo: ",self.sueldo," antiguedad: ",self.antiguedad)




print("\n**********Persona**********")

persona1=persona("antonio",22,"Mexico")    #aqui creamos una persona cualquiera
persona1.info()



print("\n**********Empleado**********")      #un empleado siempre es una persona, pero una persona no simpre es un empleado

empleadoP=empleado(3000,"3 anios","Julio",33,"Sonora")
empleadoP.info_empleado()        


isinstance()


