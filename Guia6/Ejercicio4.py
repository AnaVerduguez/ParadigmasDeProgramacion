#4)Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).

#Creo mi lista donde guardare mis numeros ingresados por teclado
numeros_positivos= []
num=0

print("En caso de que quiera dejar de introducir numeros, ingrese un numero negativo")

#Aplicamos un while que me permita agregar un numero a mi lista numeros[]
while num >= 0:
  num= int(input("Ingrese un numero:"))

  if num < 0:
    break
  elif num >0:
    #Se agrega num a la lista
    numeros_positivos.append(num)
#Imprimo por pantalla el resultado de mi lista
print("Los numeros que si pertenecen a la lista son: {0}".format(numeros_positivos))





