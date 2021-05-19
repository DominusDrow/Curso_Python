
cont=0
contp=0

print("VERIFICACION DE CORREOS")


email=input("\ningrese su correo electronico:  ")


for i in email:

	if i== "@" :
		cont+=1

	elif i== ".":
		contp+=1

if cont==1 and contp>=1:

	print("\nCorreo valido")

else:
	print("\nCorreo no valido")




