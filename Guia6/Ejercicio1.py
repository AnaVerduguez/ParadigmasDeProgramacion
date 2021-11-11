#1)Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo

#Para poder crear mi lista uso import random una libreria que me permite generar numeros aleatorios
import random

#Creo mi funcion para volver a reutilizar mis operaciones
def calculo_valores(num):
  #Aplico un for i in range que me permite realizar 
  for numero in num:
    cuadrado= numero ** 2
    cubo= numero ** 3
    print(numero,"Su cuadrado es: {0} y su cubo es: {1}".format(cuadrado,cubo))

#Creo mi lista con numero aleatorios del 1 al 10
valores = []
#Asigno los numeros random a mi lista, asigno los parametros (1,11) ->1 al 10
for asignar in range(1,11):
	valores.append(random.randint(1,10))
calculo_valores(valores)
  
