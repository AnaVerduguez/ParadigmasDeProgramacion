#5)Se dispone de un lote de valores enteros positivos que finaliza con un número negativo. El lote está dividido en sublotes por medio de valores cero. Desarrollar un programa que determine e informe:
#a)	por cada sublote el promedio de valores
#b)	el total de sublotes procesados
#c)	el valor máximo del conjunto, indicando en que sublote se encontró y la posición relativa del mismo dentro del sublote
#d)	valor mínimo de cada sublote

#Nota: el lote puede estar vacío (primer valor negativo), o puede haber uno, varios o todos los sublotes vacíos (ceros consecutivos) 

#Inicializo las variables a utilizar
numero= 1
sublote= 0
sublote_suma= 0
posicion_numero= 0

numeros_ingresados= 0
promedio_sublotes= 0

maximo= 0
sublote_max= 0
sublote_posicion=0

minimo= 0

print("Ingrese valores enteros al lote, en caso de que quiera pasar al siguiente sublote debe ingresar 0. Para finalizar el programa debe ingresar un valor negativo")

#El numero se inicializa en 1 para que pueda entrar al bucle while
#Mientras que el numero no sea negativo:
while numero >=0:
  #Aplicamos un contador para saber en que posicion se encuentra el numero
  posicion_numero= posicion_numero + 1
  numero= int(input("Ingrese un valor:"))
  if numero >0:
    #aplicamos un acumulador para sumar los sublotes
    sublote_suma= sublote_suma + numero
   
  #c)Valor maximo del conjutno
  #Aplicamos la formula para sacar el maximo
  if maximo == 0:
    maximo = numero
  
  if numero>maximo:
    maximo = numero

  #Sublote maximo lo guardamos para saber en que sublote se encuentra
  sublote_max= sublote + 1
  #Posicion en la que se encuentra el sublote
  sublote_posicion= posicion_numero

  #d)Valor minimo del sublote
  #Aplicamos la formula de minimo

  if minimo==0:
    minimo= numero

  if numero < minimo:
    minimo = numero

  #Creamos una variable en donde guardamos la cantidad de numeros que el usuario ingreso
  numeros_ingresados= numeros_ingresados +1 

  #En caso de que el numero sea 0, osea que se quiera pasar de sublote
  if numero == 0:
    sublote= sublote + 1

  #a)Por cada sublote el promedio de valores
  promedio_sublotes= sublote_suma / numeros_ingresados

  #Para ingresar en otro sublote debo de reiniciar los valores
  sublote_suma= 0
  numeros_ingresados= 0
  posicion_numero= 0 
  minimo=0

  if numero < 0:
    break
  
print("a)El promedio de valores por cada sublote es: {0}".format(promedio_sublotes))
print("b)El total de lotes procesados es: {0}".format(sublote))
print("c)El valor maximo es {0} ubicado en el sublote{1} con posicion {2}".format(maximo,sublote_max,sublote_posicion))
print("d)El valor minimo del sublote {0} es {1}".format(sublote,minimo))