#3)Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.

#Defino mi variable y mi lista
numero = 0
numeros= []

#Pido que el usuario ingrese por teclado los numeros y los valido. Luego lo ingreso en la lista
print("Bienvenido, debera ingresar un conjunto de valores, en caso de que quiera finalizar la carga ponga -1")

while numero != -1:
    numero= float(input("Ingrese un numero: "))
  #Creo un break que me finaliza el programa si se me carga -1
    if numero == -1:
      break
    else:
      numeros.append(numero)

#Creo mi funcion con las operaciones a realizar
def calculo_de_numeros (lista_de_numeros):
  cantidad = 0
  suma = 0
  promedio = 0

  cantidad = len(lista_de_numeros)

  suma = sum(lista_de_numeros)

  promedio = suma / cantidad

  return cantidad,suma,promedio

#Aplico una tupla que me permite saber la posicion en la que se encuentra cada calculo
tupla = calculo_de_numeros(numeros)

print("La cantidad de numeros que se ingresaron fueron: {0}".format(tupla[0]))
print("La suma total de los numeros es: {0}".format(tupla[1]))
print("El promedio es: {0}".format(tupla[2]))

