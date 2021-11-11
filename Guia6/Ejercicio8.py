#8)Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos: Todos los alumnos mayores de edad y los alumnos mayores (los que tienen más edad)

#Defino mis variables
nombre= ""
edad=0
maximo= 0

#Creamos dos listas con los datos
nombres_alumnos= []
edades_alumnos= []

#Aplico un while para que el programa termine si ingresa un * en nombre
print("En caso de que quiera dejar de cargar datos debera ingresar * en nombre")

while nombre != "*":
  nombre= input("Ingrese el nombre del alumno:")
  edad= input("Ingrese la edad del alumno:")
  nombres_alumnos.append(nombre)
  edades_alumnos.append(edad)

  #Uso el break para terminar el programa
  if nombre == "*" or edad == "*":
    break

#Esto me permite saber la edad maxima que se ingreso
maximo= max(edades_alumnos)
print("El mayor es el de {0} años".format(maximo))

#Por otro lado, tenemos que saber cuales son los mayores de edad para eso aplico un for i y adentro un if con una condicion
#El zip me permite utilizar las dos listas al mismo tiempo
for nombre,edad in zip(nombre,edad):
	if len(edad) >= 18:
		print(nombre)

  





