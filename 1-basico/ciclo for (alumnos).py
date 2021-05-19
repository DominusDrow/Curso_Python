

alumnos=[]
j=0

print("REGISTRO DE ESTUDIANTES:\n")

cont=int(input("cuantos alumns registrara? "))

while j<cont:

	alumnos.append(input("\tinserte el alumno: "))
	j+=1



print("\nLos alumnos ingresados fueron:\n ")

for i in alumnos:
	print(i)


