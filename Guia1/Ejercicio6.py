#Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, en una única línea, con espacios intermedios. Ayuda: Investigar acerca del parámetro end de la función print

palabra= input("Ingrese una palabra:")

for i in range (1001):
  #end=" " -> Nos ayuda a imprimir una secuencia de valores en una misma linea y evita el salto de linea
 print (palabra ,end=" " )

