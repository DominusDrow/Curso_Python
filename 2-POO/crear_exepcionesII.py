import math

def raiz(num):

	if num<0:

		raise ValueError ("no hay raices negarivas dahh") #aqui cramos una excepcion a proposito

	else:

		return math.sqrt(num)


print("\nCalcular raices cuadradas\n")

num=int(input("ingrese el valor a calcular: "))

try:
	
	print("\nla raiz es: "+str(raiz(num)))

except ValueError as no_hay_raices_negativas: 

	print(no_hay_raices_negativas)  #aqui la controlamos :b


print("\nPrograma finalizado")