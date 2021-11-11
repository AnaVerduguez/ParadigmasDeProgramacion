#Tema 1:Del censo realizado en una poblacion se conocen los siguientes datos:
#a)Dia de nacimiento (2 digitos)
#b)Mes de nacimiento (2 digitos)
#c)Año de nacimiento (2 digitos)
#d)Sexo (M:Masculino / F:Femenino)
#Con estos datos de cada habitante se forma un lote finalizado con un dia cero. Desarrollar el programa que determine e imprima:
#a)Cuantos nacimientos hubo en el mes de octubre de todos los años.
#b)Cuantos nacimientos hubo antes del 9 de julio de 1970.
#c)Cuantos nacimientos de mujeres hubo en la primavera(sabiendo que primavera es la estacion del año que va desde 22 de septimbre a 21 de diciembre) de 1942.
#d)Sexo de la persona mas anciana.
#Realizar un menu de opciones y ademas una opcion que indique la salida del programa
#El codigo debera ser comentado indicando la logica de la solucion y debera estar cargado en repl.it.

#Declaro mis variables a utilizar
continuar= True
contador_nacimientos= 0
contador_nacimientos2= 0
contador_nacimientos3= 0
sexo_anciana= 0

#Le pido al usuario que ingrese los datos necesarios para luego realizar las operaciones en el menu de opciones
dia= int(input("Ingrese el dia de nacimiento(2 digitos):"))
mes= int(input("Ingrese el mes de nacimiento(2 digitos):"))
año= int(input("Ingrese el año de nacimiento(2 digitos):"))
sexo= str(input("Ingrese el genero(F o M:)"))

if (dia or mes or año or sexo == 0):
 print("Ingrese un valor correcto")
  break

#Muestro un menu de opciones para que el usuario elija la opcion que desee 
print("MENU DE OPCIONES:")
while (continuar == True):
  print("1)Nacimientos que hubo en el mes de octubre de todos los años.")
  print("2)Nacimientos que hubo antes del 9 de julio de 1970.")
  print("3)Nacimientos de mujeres hubo en la primavera de 1942.")
  print("4)Sexo de la persona mas anciana.")
  print("5)Salir del programa.")
  
  ingreso= int(input("Ingrese la opcion que usted desee: "))
  #En caso de que la opcion ingresada sea 0, se finaliza el programa
  if (ingreso == 0 ):
    continuar = False

  #PUNTO A 
  #Si el usuario elije la opcion 1) entonces: 
  #En caso de que los nacimientos sean en el mes de Octubre, se suman todos en una variable llamada contador_nacimientos
   if (ingreso == 1):
     if (mes == 10):
       contador_nacimientos= contador_nacimientos + 1

  #PUNTO B
  #Si el usuario elije la opcion 2) entonces:
  #En caso de que los nacimientos sean antes del 9 de julio de 1970, se suman todos en una variable llamada contador_nacimientos2 
   if (ingreso == 2):
    if (año <70 and mes<7 and dia<9):
      contador_nacimientos2= contador_nacimientos2 + 1

  #PUNTO C
  #Si el usuario elije la opcion 3) entonces:
  #En caso de que los nacimientos de mujeres sean durante la primavera 1942, se suman en una variable llamada contador_nacimientos3. 
  #Primavera -> Del 22/09 hasta el 21/12
   if(ingreso == 3):
     if (sexo == "F" and año == 42):
       if (dia >= 22 and mes >= 9):
         contador_nacimientos3= contador_nacimientos3 + 1
       if (dia <= 21 and mes <= 12):
         contador_nacimientos3= contador_nacimientos3 + 1
    
 #PUNTO D
 #Si el usuario elije la opcion 4) entonces:
 #Se muestra el sexo de la persona mas anciana
  if(año>)



else:
  print("Saliendo del menu de opciones.")

#Imprimo por pantalla los resultados de mis operaciones realizadas
print("La cantidad de personas nacidas en el mes de Octubre de todos los años son:" ,contador_nacimientos)
print("La cantidad de personas nacidas antes del 9 de Julio de 1970 son:" ,contador_nacimientos2)
print("La cantidad de mujeres nacidas en la primavera de 1942 son:" ,contador_nacimientos3)
print("El sexo de la persona mas anciana es:" ,sexo_anciana)