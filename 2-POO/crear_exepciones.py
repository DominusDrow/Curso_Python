
def validar_edad(edad):

	if edad <0:
		raise NameError ("NO Existes hahaha") #aqui se genera una excepcion a proposito

	elif edad <20:
		return "disfruta la vida :)"

	elif edad <40:
		return "Ya estas viejo"

	elif edad <80:
		return "cuidate"

	elif edad <100:
		return "si se puede"

	else:
		return "ya la estas esperando"

print("\nPrograma que valida la edad \n")

edad=int(input("ingrese su edad: "))	


print(validar_edad(edad))


print("\nProbrama finalizado")