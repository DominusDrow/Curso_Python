

def media(lista,m):
	n=0
	s=0

	while n<m:
		s+=lista[n]   
		n+=1
	return s/m

n=0
lista=[0,0,0,0,0,0,0,0,0]

print("PROGRAMA QUE SACA LA MEDIA: ")

m=int(input("Cuantos valores seran?: "))

while n<m:
	lista[n]=int(input("Ingrese el valor: "))
	n+=1

print("\nla media aritmetica es: ",media(lista,m) )