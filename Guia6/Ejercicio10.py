#10)Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

import random

#Defino mi lista
#Una matriz es un arreglo que almacena multiples valores en una sola variable. Esta compues por filas y columnas
matriz= []

#Defino los parametros de mi matriz
filas= 5
columnas= 5

#Le agrego a mi matriz los diferentes numeros aleatorios que importe con el metodo random
#len() devuelve la longitud de un objeto
#La matriz esta acompañada a su vez por una submatriz dentro de ella
while len(matriz) < filas:
  sub_matriz= []

  #los numeros van del 1 al 10
  for i in range(columnas):
    numeros= random.randint(1,10)
    sub_matriz.append(numeros)
  matriz.append(sub_matriz)

#A partir de las listas puedo crear una funcion que me cree la tabla 

def tabla(matriz):
  print("ESTA ES LA TABLA")
  for i in range(len(matriz)):
    for f in range (len(matriz[0])):
      #Estructura que me permite imprimir la matriz-> (Lista de lista)
      #end= " " me permite NO dar un salto de linea 
      print(matriz[i][f], end=' ')
    print()

#Def que me permite sumar las filas de mi matriz
def sumatoria_filas(matriz):
  suma= 0
  for i in range(len(matriz)):
    for r in range(filas):
      suma= suma + matriz[i][r]
     #Se suman las filas
    matriz[i].append(suma)
    suma= 0

#Def que me permite sumar las columnas de mi matriz
def sumatoria_columnas(matriz):
  fila2=[]
  for i in range(columnas):
    suma = sum([columna[i] for columna in matriz])
    fila2.append(suma)
  matriz.append(fila2)

#Luego de finalizar mis operaciones dentro de los def imprimo por pantalla los resultados de mi tabla
sumatoria_columnas(matriz)
sumatoria_filas(matriz)
tabla(matriz)

    
  

