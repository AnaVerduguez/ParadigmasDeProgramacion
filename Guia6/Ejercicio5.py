#5)Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.

#Volvemos a utilizar el modulo random que me otorga valores aleatorios
import random

#Creamos nuestra lista
numeros_aleatorios= []

#Utilizo un for i in range porque solamente necesito 10 valores
for i in range(1,11):
  #Le agrego numeros aleatorios del 1 al 100
  numeros_aleatorios.append(random.randint(1,100))

#Este modelo me permite ordenar los numeros de mayor a menor
numeros_aleatorios.sort()
#imprimo por pantalla el resultado de mi lista
print(numeros_aleatorios)