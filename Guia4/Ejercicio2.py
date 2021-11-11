#2)Dados N valores informar el mayor, el menor y en que posición del conjunto fueron ingresados.

numero_mayor= 0
numero_menor= 0
posicion_mayor= 0
posicion_menor= 0
salida= False
contador= 0

#Aplico un while para que el usuario me indique en que momento quiere salir del programa
while salida == False:
  #utilizo un contador para saber en que posicion se encuentra el numero mayor o menor
  contador= contador + 1
  numero= int(input("Ingrese un valor:"))
 
 #Estructuras principales de maximos y minimos que igualan mi numero a 0 para luego ser utilizado 
  if numero_mayor == 0:
    numero_mayor = numero
    posicion_mayor = contador
  
  if numero_menor == 0:
    numero_menor = numero
    posicion_menor = contador
  
  #Si el numero que ingresa el usuario es mayor que el numero ingresado anteriormente entonces se guarda en un contador
  if numero > numero_mayor:
    numero_mayor= numero
    posicion_mayor = contador
  
  if numero < numero_menor:
    numero_menor= numero
    posicion_menor = contador

  opcion= input("Deseas salir del programa? Si/No:").upper()
  if opcion == "SI":
    salida = True

print("El valor mayor es {0} y esta ubicado en la posicion {1}. El valor menor es {2} y esta ubicado en la posicion {3}".format(numero_mayor,posicion_mayor,numero_menor,posicion_menor)) 

  
