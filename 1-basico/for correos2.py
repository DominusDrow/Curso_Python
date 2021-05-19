
v=False

print("VALIDAR CORREO:\n")

email=input("ingrese su correo: ")


for i in range(len(email)):

	if email[i]=="@":
		v=True


if email:

	print("\nCorreo valido")

else:
	print("\nCorreo invalido\n")


# Otra notacion diferente es:
	          #desde donde, hasta dode, de cuanto en cuanto
for i in range(4,11,2): 

	print(f"valor de {i}")

