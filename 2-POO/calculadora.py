
def suma(n,m):

	return n+m

def resta(n,m):

	return n-m

def multi(n,m):

	return n*m

def div(n,m):

	try:
		return n/m

	except ZeroDivisionError:

		print("\nno se puede dividir por 0")

		return "operacion no valida"


operaciones=(suma,resta,multi,div)

print("CALCULADORA SIMPLE\n")

op=input("suma\nresta\nmulti\ndiv\nSelecione la operacion a realizar: ")

while True:

	try:
		n=int(input("ingrese el valor 1: "))
		m=int(input("ingrese el valor 2: "))
		break

	except ValueError:

		print("\nValores incorrectos, intente de nuevo\n")

if op=='suma':

	op2=suma(n,m)

elif op=='resta':

	op2=resta(n,m)

elif op=='multi':

	op2=multi(n,m)

elif op=='div':

	op2=div(n,m)

else:

	print("\nOpcion no registrada\n")


print('\nel resultado es: '+str(op2))


print("\nPrograma finalizado")

