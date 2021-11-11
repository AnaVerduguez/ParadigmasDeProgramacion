#5)Se pide que implemente el procedimiento ReparandoLaNave(). Teniendo en cuenta que el marciano de la imagen debe llegar a su hogar con suficiente combustible, se pide que recorra el camino indicado, teniendo en cuenta que en el medio se puede encontrar con combustible, el cual, es representados por celdas Rojas y Negras. El combustible podría estar en cualquier parte del camino. Si el combustible es Rojo, nuestro amigo el marciano se detendrá y dejará una mancha Verde en el lugar, debido a que encontró combustible de calidad, pero luego seguirá su camino. Si el combustible es Negro, podrá avanzar sin problemas. El camino tiene 5 celdas de ancho

print("El marciano debe de llegar a su casa y para eso hay que tener en cuenta:")
print("""
      R -> se carga combustible dejando una mancha verde
      N -> se carga combustible sin dejar ninguna mancha
      B -> espacio en blanco
      V -> mancha por combustible de calidad
      """)

#Primero creamos la funcion correspondiente
def ReparandoLaNave():
  filas= 7
  columnas=5

  #Debemos de crear una lista donde guarde el camino normal de la imagen. Para eso debemos de crear listas adentros de una lista
  #Hay 7 filas y 5 columnas en total
  camino_inicial= [ ["R","B","N","B","R"],
                    ["B","B","B","B","B"],
                    ["R","N","B","R","N"],
                    ["B","B","B","B","B"],
                    ["N","B","R","B","N"],
                    ["B","B","B","B","B"],
                    ["R","B","R","B","N"] ]
  
  for i in range(7):
    for p in range(5):
      if camino_inicial [i][p] == "R":
        camino_inicial [i][p]= "V"
      print(camino_inicial[i][p], end=" ")
      
ReparandoLaNave()
