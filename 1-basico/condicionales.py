
cargos=("presidente","gobernador","municipal","policia")
sueldos=[0,0,0,0]

i=0

while i<len(cargos) :

	print("Suledo de el "+cargos[i]+":")
	sueldos[i]=int(input())
	i+=1

if sueldos[3]<sueldos[2]<sueldos[1]<sueldos[0]:
	print("\nTodo en orden")

else:
	print("\nojo ahi")
