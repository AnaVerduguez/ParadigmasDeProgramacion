#5)Dados dos valores enteros y distintos, emitir una leyenda apropiada que informe cuál es el mayor entre ellos.

#Le pido al usuario que ingrese por teclado dos valores enteros diferentes
valor_uno= int(input("Ingrese un valor entero:"))
valor_dos= int(input("Ingrese otro valor entero diferente al primero:"))

#Aplico el condicional IF y ELSE, en caso de que el valor 1 sea mayor que el valor 2 se imprime por pantalla que es mayor,caso contrario se imprime por pantalla que es menor.
if valor_uno > valor_dos:
  print("El numero" ,valor_uno ,"es mayor que el numero" ,valor_dos)
else:
  print("El numero" ,valor_uno ,"es menor que el numero" ,valor_dos)
