#5)Ingresar e informar valores, mientras que el valor ingresado no sea negativo. Informar la cantidad de valores ingresados

#Inicializo las variables en 0
numero= 0
contador=0

#Utilizamos el while not para que en el caso de que el numero ingresado sea menor a 0 se termina el programa.En caso de que el numero sea mayor a 0 se suma con el contador
#Traduccion: Mientras que el numero NO sea menor a 0...
while not numero < 0:
   numero= int(input("Ingrese un numero que no  sea negativo:"))
   if numero > 0:
     contador= contador + 1

print("La cantidad de valores ingresados fueron:" ,contador)