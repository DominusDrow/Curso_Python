
tuplap=("alfred",19,"tauro",2001,"DominusDrow")

print(tuplap)
print(tuplap.count(19))

#empaquetado de tuplas
nombre,edad,signo,anio,AKA=tuplap

print("\n",nombre)
print(edad)
print(signo)
print(anio)
print(AKA)

milista=list(tuplap)
print(milista)

litap=["jajaja","prueba",2]
tuplap=tuple(litap)

print(tuplap)
print(len(tuplap))



#si se permite en "index" en tuplas

print(tuplap.index("prueba"))

