#3)Dada una serie de números enteros, informar:
#)a)su factorial
#)b)cuantos múltiplos de 3
#)c)cuantos múltiplos de 5
#)d)cuantos múltiplos de 3 y de 5
#Utilice las funciones de ejercicios anteriores.

numero= int
cont_3= 0
cont_5= 0
cont_3y5= 0

#a)Su factorial
def factorial(n):
  factorial= 1
  for i in range(1,n + 1):
    factorial = factorial * i
  return factorial

#b),c) y d) Multiplos
def maximo_comun_divisor(a,b):
  resto = -1
  while resto != 0:
    resto = a % b
    if resto == 0:
      return b
    else:
      a = b
      b = resto

#Repito la ejecucion hasta que se ingrese un num negativo. Dejo de cargar numeros
print("Para dejar de cargar numero ponga un num negativo")
while numero:
  numero= int(input("Ingrese el numero:"))
  if numero < 0:
    break

  #Utilizo las funciones con lo que me pide el ejercicio
  #b)Si es multiplo de 3
  multiplo_3= maximo_comun_divisor(3,numero)
  #b)Si es multiplo de 3
  multiplo_5= maximo_comun_divisor(5,numero)

  #Aplico los acumuladores fuera del def para saber la cantidad de multiplos que hay en total
  if multiplo_3 == 3:
    cont_3 = cont_3 + 1
  if multiplo_5 == 5:
    cont_5 = cont_5 + 1
  if multiplo_3 == 3 and multiplo_5 == 5:
    cont_3y5 = cont_3y5 + 1

#Imprimo por pantalla los resultados
print("El factorial del numero {0} es {1}".format(numero,factorial(numero)))
print("Los multiplos de 3 son {0}".format(cont_3))
print("Los multiplos de 5 son {0}".format(cont_5))
print("Los multiplos de 3 y 5 son {0}".format(cont_3y5))