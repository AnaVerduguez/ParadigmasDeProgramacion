#11)Escribir un algoritmo que resuelvan los siguientes problemas: a) Dado un número entero n, indicar si es par o no. b) Dado un número entero n, indicar si es primo o no. 

numero= int(input("Ingrese un numero entero:"))

#Indicar si es par o no
#Utilizamos el operador % para obtener el residuo de la division, sabemos que si el residuo de nuestra division da 0 el numero es par, caso contrario es impar.
if (numero % 2) == 0:
 print("El numero es par")
elif (numero % 2) != 0:
 print("EL numero es impar")

#Indicar si es primo o no
#Un numero primo solamente se puede dividir por 1 y por si mismo arrojando de resto resto 0, ademas tiene que ser mayor a 1
#Aplicamos un bucle for en donde dividimos al numero por todos los anteriores a el hasta llegar al 1
#Aplicamos un contador que sume los restos 0. Si el contador llega a 2 quiere decir que el numero es primo, caso contrario no es primo
contador= 0
for i in range (1,numero + 1):
  if (numero % i) == 0:
   contador= contador + 1
if contador == 2 and numero > 1:
  print ("El numero es primo")
elif contador != 2:
  print("El numero no es primo")

   