#7)Dado un valor M determinar y emitir un listado con los M primeros múltiplos de 3 que no lo sean de 5, dentro del conjunto de los números naturales.

#Multiplos -> Numeros naturales que se obtienen al multiplicar dicho numero por todos los numeros naturales. Para saber si es multiplo el resto nos debe de dar 0

valor_m= int(input("Ingrese un valor:"))

print("Los multiplos que son de 3 y que no son de 5 son:")

#En caso de que el numero sea multiplo de 3 y no de 5 a la vez se imprime por pantalla el resultado

for i in range (1,valor_m+1):
  if (i % 3 == 0 and i % 5 !=0):
   print(i)    
    

