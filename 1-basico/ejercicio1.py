
def DevuelveMax(num1,num2):

	if(num1<num2):
		return num2
	elif(num1>num2):
		return num1
	else:
		return -100000000000


print("EJERCICIO QUE DEVUELVE UN MAXIMO")

num1=int(input("ingrese el numero 1: "))
num2=int(input("ingrese el numero 2: "))


if(num1==DevuelveMax(num1,num2)):
	print("\n El numero mayor es el numero ",num1)

elif(num2==DevuelveMax(num1,num2)):
	print("\n El numero mayor es el numero ",num2)

else:
	print("\n Los numeros son iguales")


print("\n El programa ha finalizado")