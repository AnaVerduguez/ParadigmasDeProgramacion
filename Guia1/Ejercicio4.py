#Implementar un algoritmo que, dado un número entero 𝑛, permita calcular su factorial.

numero_entero= int(input("Ingrese un numero entero:"))

#Utilizo la funcion integrada en Python para averiguar la factorial de un numero
from math import factorial
print("La factorial de" ,numero_entero ,"es" ,factorial(numero_entero))

