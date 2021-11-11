#Escribir un programa que imprima por pantalla todas las fichas de dominó, de una por línea y sin repetir. 

print("Las fichas de domino son:")
#Toma los parametros del 0 al 6, ya que las fichas del domino solo van hasta el n°6
for i in range(0,7):
  for j in range(0,7):
    print(i,"|" ,j)


