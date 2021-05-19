
listap=["hola","cuantos","años","tienes"]

print(listap[0])

print(listap[2:])

print(listap[:])


listap.append("tu:")
print(listap[:])

listap.insert(0,"jaja")
print(listap[:])


listap.extend(["yo","tengo","15","años"])
print(listap[:])

print(listap.index("tengo"))

print("15" in listap)

listap.remove("jaja")
print(listap[:])

listap.pop()
print(listap[:])


listap1=["años",":c"]

listap+=listap1
print(listap[:])

