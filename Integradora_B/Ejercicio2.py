#2) Una empresa que distribuye mercadería hacia distintas localidades del interior dispone de dos lotes: Uno denominado DESTINOS con información de la distancia a cada uno de los destinos:
#a) Nro. de destino (3 dígitos)	
#b) Distancia en kilómetros (NNN.NNN)
#Otro denominado VIAJES con los viajes realizados por cada camión (< 200), donde cada registro contiene:
#a) Patente del camión (6 caracteres)	
#b) Nro. de destino	
#c) Nro. de chofer (1 a 150)
#Desarrollar estrategia, algoritmo y codificación del programa que determine e imprima:
#1) Cantidad de viajes realizados a cada destino (solo si > 0).
#2) Nro. de chofer con menor cantidad de Km (entre los que viajaron).
#3) Patente de los camiones que viajaron al destino 116 sin repeticiones de las mismas.

#Comienzo creando mis listas
#Lote de DESTINOS
lista_destino= []
lista_kilometros= []
#Lote de VIAJES
lista_patente= []
lista_166= []
lista_encargo= []
lista_chofer= []

#Creo mis variables
contador= 0
minimo= 0
chofer_menor= 0
#Creo mi funcion
def registros(nro_destino, kilometros,patente,nro_encargo,nro_chofer,minimo):
  contador= 0
  nro_destino= int(input("Ingrese el numero del destino. SOLO 3 DIGITOS:"))
  lista_destino.append(nro_destino)

  while nro_destino != 3:
    break
    print("ingrese un destino correcto")
  
  kilometros= int(input("Ingrese la distancia en KMS. SOLO FORMATO (NNN.NNN):"))
  lista_kilometros.append(kilometros)

  patente= int(input("Ingrese la patente del camion. SOLO 6 CARACTERES:"))
  lista_patente.append(patente)
  while patente != 6:
    break
    print("ingrese una patente correcta")
  
  nro_encargo= int(input("Ingrese el numero de destino: "))
  lista_encargo.append(nro_encargo)

  #Punto 1
  if nro_encargo >0:
    contador= contador + 1

  #Punto 3
  if nro_encargo == 116:
    lista_166.append(patente)

  nro_chofer= int(input("Ingrese el numero del chofer. SOLO DEL 1 AL 150:"))
  lista_chofer.append(nro_chofer)
  
  #Punto 2
  if kilometros < minimo:
    minimo= kilometros
    chofer_menor = nro_chofer

  if nro_encargo >0:
    opcion= input("Desea seguir cargando registros? SI o NO").upper
    while opcion == "NO":
      break

registros(lista_destino,lista_kilometros,lista_patente,lista_encargo,lista_chofer,minimo)

print("RESULTADOS:")
print("Se hicieron {0} viajes en total:" .format(contador))
print("El chofer con menos KMS es: {0}".format(chofer_menor))
print("Las patentes que viajaron al destino 166 son: {0}".format(lista_166))
  

      





