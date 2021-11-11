#2)Desarrollar una función tal que dado un  número entero positivo calcule y retorne su factorial.

#Factorial de un num ->Producto de todos los enteros positivos menores o iguales a ese num. Un multiplicacion continua

numero= int(input("Ingrese un numero entero positivo:"))

def factorial(n):
  #La factorial simpre debe empezar por 1
  factorial= 1

  #Utilzamos un for i in range. Empieza desde el 1 hasta el n incluyendolo.
  for i in range(1,n + 1):
    factorial = factorial * i
  
  #Siempre debo de devolver la funcion
  return factorial

print("El factorial es:" ,factorial(numero))