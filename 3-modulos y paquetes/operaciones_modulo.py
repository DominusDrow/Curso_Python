
'''import modulo_operaciones    #esta es una manera de importar aunque se tiene que tratar como objeto


print(modulo_operaciones.pote(2,5)) 

'''

'''
from modulo_operaciones import pote     #esta es otra forma en donde se especifica que funcion se va a importar

print(pote(2,6))

'''

from modulo_operaciones import *     #cuando se pone asterisco indicamos que se importar el modulo completo


print("\nEsta es una suma: ",suma(3,4))

print("\nEsta es una potencia: ",pote(3,4))

print("\nEsto es una multiplicacion: ",multi(23,39))