#12. Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
#Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
#1.	  111111111111111
#2.	  100000000000001
#3.	  100000000000001
#4.	  100000000000001
#5.	  111111111111111
#Visualiza el contenido de la matriz en pantalla.

#Creo mi lista
matriz= []

#Defino los parametros de mi lista
filas= 5
columnas= 15

#Aplicamos un bucle para validar los parametros
#len() devuelve la longitus del objeto
for i in range(filas):
  sub_matriz= []
  for r in range(columnas):
    if i == 0 or i == 4:
    #En este caso toma el valor de 1 ya que es diagonal
      sub_matriz.append(1)
    elif r == 0 or r == 14:
      sub_matriz.append(1)
      #En este caso toma el valor 0 ya que no es diagonal
    else:
      sub_matriz.append(0)
  matriz.append(sub_matriz)

def tabla(matriz):
    print("ESTA ES LA TABLA")
    for i in range(len(matriz)):
      for f in range (len(matriz[0])):
      #Estructura que me permite imprimir la matriz-> (Lista de lista)
      #end= " " me permite NO dar un salto de linea 
        print(matriz[i][f], end=' ')
    print()

tabla(matriz)


    



