#4)Dado un conjunto de valores, que finaliza con un valor nulo, determinar e imprimir (si hubo valores):
#a) El valor máximo negativo
#b) El valor mínimo positivo
#c) El valor mínimo dentro del rango -17.3 y 26.9
#d) El promedio de todos los valores.

numero = float
contador = 0 
maximo_negativo = 0
minimo_positivo = 0
minimo_rango = 0
promedio=float
suma_numeros= 0

print("Ingrese un conjunto de numeros, para finalizar el ingreso ponga 0")

while numero != 0:
  numero=float(input("Ingrese un numero: "))
  
  #Aplico el break para que el programa deje de funcionar si se ingresa un 0
  if numero == 0:
    break
  
  #a) El valor máximo negativo
  if numero < 0:
    #Si es negativo entra al condicional
    if maximo_negativo == 0:
      maximo_negativo = numero

    if numero > maximo_negativo:
      maximo_negativo = numero
  
  #b)El valor mínimo positivo
  if numero > 0:
    #Si es positivo entra al condicional
    if minimo_positivo == 0:
      minimo_positivo = numero

    if numero < minimo_positivo:
      minimo_positivo = numero

  #c) El valor mínimo dentro del rango -17.3 y 26.9
  if numero >= -17.3 and numero <= 26.9:
    
    if numero < minimo_rango:
      minimo_rango = numero
  
  #Se suman todos los numeros en una variable suma_numeros, esto lo hacemos para sacar el promedio. El contador nos sirve para saber la cantidad de numeros que se ingresaron.
  suma_numeros = suma_numeros + numero
  contador = contador + 1

#Promedio-> El total de los numeros dividido por la cantidad de numeros  
  promedio = (suma_numeros/ contador)


print("a)El valor máximo negativo es {0}".format(maximo_negativo))
print("b)El valor mínimo positivo es {0}".format(minimo_positivo)) 
print("c)El valor mínimo dentro del rango -17.3 y 26.9 es {0}".format(minimo_rango)) 
print("d)El promedio de todos los valores es {0}".format(promedio))

