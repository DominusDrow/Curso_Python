
cont=0

print("no contar los espacios:\n")

palabra=input("Ingrese una frase: ")

for i in palabra:

	if i==" ":
		continue

	cont+=1

print(f"\nEl numero de letras que tiene la frase es de {cont} ")

print("\n\nEjemplo del else:\n")

f=input("ingrese una palabra que contenga @: ")

for i in f:

	if i=="@":
		print("texto correcto")
		break

else:
	print("Texto incorrecto")