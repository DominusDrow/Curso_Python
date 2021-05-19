
#primero haremos el ejercicio con bucles anidados

def palabras(*palab):	#con esta sintaxis la funcion recibe como parametro una serie indefinida de elementos (*)
						#tambien todo lo recibe como tuplas
	for p in palab:  
		for subp in p:
			yield subp



arreglo=palabras("hola","como","estas", "yo bien")

print(next(arreglo))

print("\nAQui va mas codigido //////")

print(next(arreglo))

print("\nAQui va mas codigido //////")

print(next(arreglo))

print("AQui va mas codigido //////\n")

print(next(arreglo))


#ahora lo hacemos con yield from


def palabras2(*palabras):

	for p in palabras:

		yield from p




develve=palabras2("este","es","otro","ejemplo")


print("\n\n*******OTRA FORMA*******\n")

print(next(develve))

print("\nAqui va mas codigo")

print(next(develve))

print("\nMAs codigo")

print(next(develve))