
def generar_pares(lim):

	i=1

	while i<lim:

		yield i*2

		i+=1



lista=generar_pares(10)


print(next(lista))


print("taran taran taran")

print(next(lista))	


print("taran taran taran")

print(next(lista))	