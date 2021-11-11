#3)Se pide que defina el procedimiento CaballoRojoCapturarPosición1() que permita realizar el movimiento del caballo hacia la posición 1 de la figura y capturar una pieza rival si existe. Para esto considere que: 
#● El movimiento característico del “Caballo” es en forma de una L de 2x3 o 3x2 casilleros (contando el casillero de partida). 
#● El caballo además tiene la cualidad (única entre todas las piezas) de poder “saltar” piezas, de forma que puede pasar a través de casilleros donde exista una pieza para llegar a su destino. 
#● Para que el caballo rojo pueda capturar una pieza rival en la posición 1, debe existir en la posición 1 una ficha rival.
#● En este caso el caballo rojo toma el lugar de la pieza rival (la pieza rival es removida del tablero y el caballo queda en el lugar donde estaba la pieza rival). 
#● En caso contrario, o sea si no hay pieza rival en la posición 1, el caballo no realiza ningún movimiento (se queda en el lugar de partida).
#● Además debe tener en cuenta que si el caballo toma una pieza rival, el casillero de partida debe quedar sin ninguna pieza, es decir se debe corresponder con un tablero vacío de ajedrez (en donde un casillero puede ser blanco o negro)

import random

#Defino mi funcion
#Matriz es mi lista de lista
def CaballoRojoCapturarPosición1(tablero_ajedrez):
  for j in tablero_ajedrez:
    print(j)

#Defino mi lista y las filas/columnas de mi matriz
tablero_ajedrez= []
filas= 5
columnas= 5
BLANCO= 0

#Utilizo las posiciones correspondiente de la lista para reemplazarlas 
for f in range(filas):
  tablero_ajedrez.append([0]*columnas)

for i in range(filas):
  for q in range(columnas):
    tablero_ajedrez [2][2] = "CABALLO"
    tablero_ajedrez [q][i] = random.choice(["RIVAL", "BLANCO"])

if tablero_ajedrez[4][1] == "RIVAL":
  tablero_ajedrez[1][4] = "CABALLO"
  BLANCO = 1
if BLANCO == 1:
  tablero_ajedrez [2][2] = "BLANCO"
    
CaballoRojoCapturarPosición1(tablero_ajedrez)