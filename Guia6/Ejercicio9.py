#9)Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
#La temperatura media de cada día
#Los días con menos temperatura
#Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.

#Nombro mis variables y mi lista
temperaturas=[]
dias= 5
i=1

#Utilizamos un while para ingresar 5 dias 
while dias > 0:
  num= float(input("Ingrese la temperatura del dia: "))
  #le agrego las temperaturas a mi lista
  temperaturas.append(num)
  i= i + 1
  dias= dias - 1

#Por otro lado creo mi def en donde voy a realizar las operaciones
def temperatura(a):
  mayor= max(temperaturas)
  menor= min(temperaturas)
  promedio= float(len(temperaturas))
  #imprimo los resultados por pantalla
  print("La temperatura media es: {0}".format(promedio))
  print("La temperatura mas alta es:{0}".format(mayor))
  print("La temperatura mas baja es:{0}".format(menor))
  return temperatura
print(temperatura(temperaturas))






