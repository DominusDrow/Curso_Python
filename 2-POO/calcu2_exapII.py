
def div_f():

	try:

		n1=float(input("\nIngrese el valor 1: "))

		n2=float(input("ingrse el valor 2: "))

		print("\nEL resultado es: "+str(n1/n2))

	except ZeroDivisionError:

		print("\nNo se puede dividir por 0")

	except ValueError:

		print("\nDatos incorrectos")

	finally:

		print("\nProgrma finalizado")


def div_e():

	try:

		n1=int(input("\nIngrese el valor 1: "))

		n2=int(input("ingrse el valor 2: "))

		print("\nEL resultado es: "+str(n1/n2))

	except:

		print("\nOcurrio u error :(")


	print("\nProgrma finalizado")



print("\nCalculadora con Ecepciones: \n")

op=input("1.Enteros\n2.Reales\nElija una opcion: ")

if op=="1":

	div_e()


elif op=="2":

	div_f()

else:
	print("\nOpcion no registrada")
