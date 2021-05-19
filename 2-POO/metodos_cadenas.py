#comprobando una direccion de correo electronico

print("\nComprobando direciones de correo electronico\n")

correo=input("\nIngrese su correo: ")


if correo.count("@")==1 and correo.find("@")!=0 and correo.find("@")!= len(correo)-1 :

	print("\nCorreo correctamente escrito")

else:

	print("\nCorreo incorrecto")

