import numpy as np

print("------- Llenar matriz de ceros -------")
matriz=np.zeros([3,5]) # 3 filas x 5 columnas
print(matriz)

print("------- Llenar matriz de unos -------")
matriz=np.ones([3,5]) # 3 filas x 5 columnas
print(matriz)

print("------- Llenar matriz de vaios -------")
matriz=np.empty([3,5]) # 3 filas x 5 columnas
print(matriz)

print("------- Llenar matriz de rango -------")
# El primer parametro es el valor inicial
# El segundo parametros es el valor final 
# El terecer parametro es el incremento
lista=np.arange(0,10,2) # 3 filas x 5 columnas
print(lista)

print("------- Llenar matriz de rango No 2 -------")
# El primer parametro es el valor inicial
# El segundo parametros es el valor final 
# El terecer parametro es el incremento
lista=np.arange(0,10,1) # 3 filas x 5 columnas
print(lista)