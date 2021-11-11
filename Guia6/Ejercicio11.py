#11)Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
#Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
#Muestra el contenido de la tabla en pantalla.

#Aplico la misma logica que en el ejercicio anterior, vuelvo a utilizar mis def
#Creo mi lista matriz
matriz= []

#Indico los parametros de mi tabla
filas= 5
columnas= 5

count=0

while len(matriz) < columnas:
  #vuelvo a crear la sublista
  sub_matriz= []
  for i in range (filas):
    if i == count:
      #tomara el valor 1
       sub_matriz.append(1)
    else:
      #tomara el valor 0
      sub_matriz.append(0)
  count = count + 1
  #Utilizo count para poder contar el número de veces que un elemento que aparece en mi lista
  matriz.append(sub_matriz)

#Luego configuro mi def para poder imprimir por pantalla el resultado de mi tabla
  def tabla(matriz):
    print("ESTA ES LA TABLA")
    for i in range(len(matriz)):
      for f in range (len(matriz[0])):
      #Estructura que me permite imprimir la matriz-> (Lista de lista)
      #end= " " me permite NO dar un salto de linea 
        print(matriz[i][f], end=' ')
    print()

tabla(matriz)
