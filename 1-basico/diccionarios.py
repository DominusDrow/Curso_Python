#declaracion:

diccionario_p={"nombre":"Alfredo","apellido":"Vasquez","matricula":2057903}
print(diccionario_p)
print(diccionario_p["nombre"])
print(diccionario_p["matricula"])

#insertar y quitar elementos

diccionario_p["AKA"]="DominusDrow"
print(diccionario_p)

diccionario_p["nombre"]="Ricardo"
print(diccionario_p)

del diccionario_p["AKA"]
print(diccionario_p)

diccionarrio_comp={"nombre":"Alfredo","matricula":201957903,"calificaciones":{"ingles":10,"DHPC":9,"calculo":9},"AKA":["Drow","galac"]}
print(diccionarrio_comp)
print(diccionarrio_comp["calificaciones"])

#metodos

print(len(diccionario_p))
print(diccionarrio_comp.keys())
print(diccionarrio_comp.values())
