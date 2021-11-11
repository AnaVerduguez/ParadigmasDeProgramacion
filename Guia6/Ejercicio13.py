#13 De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
#Para guardar esta información se van a utilizar dos arreglos:
#•	Nombre: Lista para guardar los nombres de los conductores.
#•	kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
#•	Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.
#Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

#Creo mis listas que me permitiran guardar los valores ingresados por teclado
cantidad_conductores = []
kms = []
total_kms = []

#Le pido al usuario que me indique el numero de conductores que se ingresara al programa
dato = int(input("Ingrese la cantidad de conductores que desea ingresar: "))

#Aplico un bucle que me permite realizar operaciones en caso de que el dato sea mayor a 0
while dato > 0:
  dato= dato - 1
  cantidad_conductores.append(input("Ingrese el nombre del conductor: "))
  #aplico otra lista en la que me guardara los kms de cada dia
  #Un for i in range para ingresar solamente 7 dias
  conductor_kms=[]
  for dias in range (7): 
    km= int(input("Ingrese los kilometros por dia: "))
    conductor_kms.append(km)
  kms.append(conductor_kms)
  conductor_kms = []

#Aplico un def que me ayudara a sumar los km 
def transporte (km):
  for q in range(len(km)):
    suma = sum(km[q])
    total_kms.append(suma)
    suma = 0

#Imprimo por pantalla los resultados finales de mi lista
  for p in range (len(cantidad_conductores)):
    print("El conductor {0} hizo {1} kms".format(cantidad_conductores[p], total_kms[p]))
  return transporte
print (transporte(kms))




