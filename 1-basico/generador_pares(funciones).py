
def generar_pares(lim):

	cont=1
	lista=[]

	while cont<lim:

		lista.append(cont*2)
		cont+=1

	return lista


lista=generar_pares(10)


print(lista)