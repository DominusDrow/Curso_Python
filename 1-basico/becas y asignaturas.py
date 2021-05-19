
print("\nBECAS Y SELECCION DE ASIGNATURAS\n\n")

asignaturas=("mate","quimica","biologia","calculo","filosofia")
datos=[0,0,0]

datos[0]=int(input("ingrese su numero de hermanos: "))
datos[1]=int(input("ingrese la distancia que viaja(en km): "))
datos[2]=int(input("ingrese el ingrso familiar mensual: "))


if datos[0]>3 and datos[1]>7 or datos[2]<5000 :
	
	print("\n\ttienes derecho a beca")

else:

	print("\n\tNo tiene derecho a beca")	


print("\n\nSelecion de asignaturas:\n")


print(asignaturas[:])
asig=input("Que asignatura desea llevar? ")
op=asig.lower()

if op in asignaturas:

	print("\nAsignatura registrada")

else:

	print("\nNo se encontro la materia")


print("\n\nprograma finalizado")
