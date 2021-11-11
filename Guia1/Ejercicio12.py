#Escribir un programa que tome una cantidad n de valores ingresados por el usuario, a cada uno le calcule el factorial (lo realizado en el ejercicio 1.4) e imprima el resultado junto con el número de orden correspondiente. 

from math import factorial

cantidades= int(input(("Ingrese la cantidad de numeros que va a ingresar: "))

for i in range(1,cantidades+1):
   factorial_num=int(input("Ingrese el numero para calcular su factorial:"))
   factorial= 1
   for j in range (2, factorial_num + 1):
     factorial *= j

print("Numero:" ,factorial_num ,"|Factorial:" ,factorial)
  
