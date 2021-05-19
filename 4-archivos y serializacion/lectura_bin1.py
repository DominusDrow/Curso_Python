
#aqui abriremos un fichero creado anteriormente

import pickle

arch_bin=open("nombres_bin","rb")

lista=pickle.load(arch_bin)

print(lista)

arch_bin.close()