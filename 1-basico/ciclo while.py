import math

print("CALCULAR RAIZ CUADRADA:\n")

raiz=int(input("ingrese el numero a calcular: "))

intentos=0


while raiz<0:

	print("\nNo hay raiz para numeros negativos\n")

	if(intentos==2):
		print("Numero de intentos superados")
		break;

	else:
		raiz=int(input("ingrese el numero a calcular: "))
		intentos+=1


if intentos<2:
	raiz=math.sqrt(raiz)
	print("\nLa raiz del numero es: "+str(raiz))
