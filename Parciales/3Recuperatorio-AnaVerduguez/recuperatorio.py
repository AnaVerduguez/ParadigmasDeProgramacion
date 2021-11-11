#Una empresa se dedica a hacer reformas en pisos y edificios. Para gestionar los proyectos que tienen en macha nos han encargado un programa del que se van a implementar. De cada proyecto se guarda un identificador, el nombre del cliente, el numero de dias paroximados que dura la reforma y lo que va costar.
#1)Implementar un codigo que indique el total que calcula lo que ha ganado la empresa con los proyectos finalizados mensualmente en un año.
#2)Implementar un codigo que muestre el identificador del proyecto que lleva mas tiempo y que no se ha terminado todavia.
#3)Implementar un codigo que indique el numero minimo de proyectos mensuales
#Realizar un menu de opciones y admas una opcion que indique la salida del programa
#El codigo debera ser comentado indicando la logica d ela solucion y debera estar cargado en repl.it

#Defino las variables que voy a usar

identificador= -1
nombre_cliente= ""
num_dias_proyecto= 0
acum_dias= 0
costo_proyecto= 0
acum_proyecto= 0
estado= ""

total_ganado= 0

mayor_proyecto= 0
mayor_identificador= 0

proyectos_mesuales= 0
numero_minimo= 0
minimo_identificador= 0

menu = "NO"

#Pido los datos de los proyectos por teclado
print("BIENVENIDO")
print("Ingrese los siguientes datos para cada proyecto en marcha de todo el año. El primer proyecto sera 1, el segundo sera 2 y asi sucesivamente.Para finalizar la carga de proyectos debera de poner 0 en identificador")

while identificador != 0:
  identificador= int(input("Ingrese el identificador del proyecto:"))
  if identificador == 0:
    break
  nombre_cliente= input("Ingrese el nombre del cliente: ").upper()

  num_dias_proyecto= int(input("Ingrese los dias estimados que durara el proyecto:"))
  acum_dias= acum_dias + num_dias_proyecto

  costo_proyecto= int(input("Ingrese el costo del proyecto:"))
  acum_proyecto= acum_proyecto + costo_proyecto

  estado= input("Si el proyecto ha finalizado ingrese TERMINADO, si aun sigue en marcha ingrese ACTIVO: ").upper()

#Luego de pedir los datos necesarios, empiezo con las operaciones
#1)Total que ha ganado la empresa con proyecto finalizados en un año

  if estado == "TERMINADO":
    total_ganado = acum_proyecto
    
#2)Identificar el proyecto que lleva mas tiempo y que no ha terminado todavia
#Aplico un maximo
  if estado == "ACTIVO":
    if mayor_proyecto == 0:
      mayor_proyecto = num_dias_proyecto
      mayor_identificador= identificador

    if mayor_proyecto < num_dias_proyecto:
      mayor_identificador=identificador
      
#3)Numero minimo de proyecto mensuales
#Promedio, cantidad de proyecto minimos que tienen que hacer en un mes para cumplir con todos los proyectos
  proyectos_mesuales= acum_dias / 30
  

#Utilizo un menu para que el usuario me indique que opcion deseas elegir
while (menu != "SI"):
  print("MENU DE OPCIONES:")
  print("1)Total que ha ganado la empresa con los proyectos finalizados mensualmente en un año: ")
  print("2)Identificador del proyecto que lleva mas tiempo y que no se ha terminado todavia: ")
  print("3)Numero minimo de proyectos mensuales: ")

  opcion= int(input("Ingrese la opcion que desee:"))

  if (opcion==1):
    print("El total que ha ganado la empresa es: {0}".format(total_ganado))

  elif (opcion==2):
    print("El proyecto que lleva mas tiempo y aun no ha terminado es: {0}".format(mayor_identificador))
  
  elif (opcion==3):
    print("El numero minimo de proyecto mensuales es: {0}".format(proyectos_mesuales))
  
  else:
    print("Ingrese una opcion correcta")
  
  menu=input("Desea finalizar el menu?SI/NO:").upper()

