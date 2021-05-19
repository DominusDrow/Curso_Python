#programa que pide una calificacion y pone si estamos aprovados o no

def calificacion(nota):

	resultado="Aprovado"

	if nota<6:

		resultado="Desaprovado"

	return resultado

print("Programa de calificaciones\n")

nota=input("ingrese la calificacion: ")


print(calificacion(int(nota)))

