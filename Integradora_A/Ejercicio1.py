#1)Escribir funciones que resuelvan los siguientes problemas: 
#a) Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400. 
#b) Dado un mes y un año, devolver la cantidad de días correspondientes. 
#c) Dada una fecha (día, mes, año), indicar si es válida o no. 
#d) Dada una fecha, indicar los días que faltan hasta fin de mes. 
#e) Dada una fecha, indicar los días que faltan hasta fin de año. 
#f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha. 
#g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días
#Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.

from calendar import monthrange
#Declaro mis variables para el Menu
ingreso= 0
continuar= bool(True)

#Comienzo a crear mis funciones que reutilizare en el codigo
#a)Dado un año indicar si es bisiesto
#Cualquier año divisible por 4 es un año bisiesto.
def año_bisiesto(año):
  bisiesto = (año % 4)
  if bisiesto == 0:
    return print ("El año es bisiesto.")
  else:
    return print ("El año no es bisiesto.")

#b)Dado un mes y un año, devolver la cantidad de días.
#El metodo monthrange nos devuelve el dia de la semana del primer dia del mes y el numero de dias del mes, para el año y mes especificados.
def dias_correspondientes(año, mes):
  dias_mes = monthrange(año, mes)[1]
  return dias_mes

#c)Dada una fecha (día, mes, año), indicar si es válida o no. 
def fecha_valida(año,mes,dia):
  #comenzamos a realizar las validaciones para saber si la fecha ingresada es correcta o no
  if año < 0:
    print("Ingrese un año correcto")
  elif mes < 0 or mes > 12:
    print("Ingrese un mes correcto")
  elif dia < 0 or dia > 31:
    print("Ingrese un dia correcto")
  
#d)Dada una fecha, indicar los días que faltan hasta fin de mes. 
def dias_faltantes_mes(año,mes,dia):
  bisiesto= (año % 4) 

  #Para saber cuantos dias faltan para terminar el mes se debe de saber cuantos dias tiene ese mes
    #Este mes tiene 29 dias en año bisiesto
  if bisiesto == 0:
    if mes == 2:
      resultado= 29-dia
    #Este mes tiene 28 dias en año no bisiesto
    if bisiesto != 0:
      if mes == 2:
       resultado= 28-dia
    #Estos meses tienen 31 dias
    if mes == mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
      resultado = 31-dia
    #Estos meses tienen 30 dias
    if mes == (mes == 4 or mes == 6 or mes == 9 or mes == 11):
      resultado = 30-dia 
  return 
#e) Dada una fecha, indicar los días que faltan hasta fin de año. 
def dias_faltantes_año(año,mes,dia):
  bisiesto= (año % 4) 
  resultado= 0
  for i in range(0,mes):
    i= i +1
    #Este mes tiene 29 dias en año bisiesto
    if bisiesto == 0:
      if i == 2:
        año= 366
        resultado= resultado + 29
    #Este mes tiene 28 dias en año no bisiesto
    if bisiesto != 0:
      if mes == 2:
        año= 365
        resultado= resultado + 28
    #Estos meses tienen 31 dias
    if mes == mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
      año= 365
      resultado= resultado + 31
    #Estos meses tienen 30 dias
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
      año= 365
      resultado= resultado + 30
  resultado = resultado - (dia + año) * -1
  return
#f)Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.

def dias_transcurridos(dia):
  bisiesto= (año % 4)  
  #Para saber cuantos dias transcurrieron hasta la fecha debemos de aplicar un for i in range que me permite saber el recorrido de los meses
  resultado= 0
  for i in range(0,mes):
    i= i + 1
    if bisiesto == 0:
      #Este mes con año bisiesto tiene 29 dias
      if i == 2:
        resultado = resultado + 29
      #Este mes sin año bisiesto tiene 28 dias
    else:
      if i == 2:
        resultado = resultado + 28
    #Estos meses tienen 31 dias
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
      resultado = resultado + 31
    #Estos meses tienen 30 dias
    elif i == 4 or i == 6 or i == 9 or i == 11:
      resultado = resultado + 30
  #Al contador resultado se le restan los dias ingresados para saber cuantos dias pasaron
  resultado= resultado - dia
  return

#g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días

def tiempo_dosfechas(dia1,mes1,año1,dia2,mes2,año2):

  bisiesto1=(año1 % 4) 
  bisiesto2=(año2 % 4) 
  resultado=0
  #Junto los años y los meses de las dos fechas
  año_total = año2 - año1
  mes_total = mes2 - mes1

  while mes_total < 0:
    año_total= año_total - 1
    mes_total= mes_total + 12
    dia_total = dia2 - dia1  

  while dia_total < 0:
    mes_total = mes_total - 1
    if bisiesto1 == 0 or bisiesto2 == 0:
      if mes1 == 2 or mes2 == 2:
        resultado= resultado + 29
      else:
        if mes1 == 2 or mes2 == 2:
          resultado = resultado + 28
  return
print("MENU")
while (continuar == True):
  print("""
  Elija la opcion que desee
  1. Saber si un año es bisiesto.
  2. Dado un mes y año devuelve la cantidad de dias.
  3. Dada una fecha la valida.
  4. Dada una fecha indica los dias que faltan hasta fin de mes.
  5.Dada una fecha indica los dias que faltan hasta fin de año.
  6. Dada una fecha indica los dias transcurridos.
  7.Tiempo transcurrido entre dos fechas.
  0.Salir del programa
  """)
  ingreso = int(input("Ingrese la opcion que desee: "))
  if ingreso == 0:
    continuar = False
  if ingreso == 1:
    año_ingresado= int(input("Ingrese un año: "))
    año_bisiesto(año_ingresado)
  if ingreso == 2:
    año_ingresado= int(input("Ingrese un año: "))
    mes_ingresado= int(input("Ingrese el numero correspondiente al mes: "))
    dias_mes = dias_correspondientes(año_ingresado,mes_ingresado)
    print("La cantidad de dias que tiene el mes son {0} dias".format(dias_mes))
  if ingreso == 3:
    año= int(input("Ingrese un año: "))
    mes= int(input("Ingrese el numero correspondiente al mes: "))
    dia = int(input("Ingrese un dia: "))
    fecha_valida(año,mes,dia)
  if ingreso == 4:
    año= int(input("Ingrese un año: "))
    mes= int(input("Ingrese el numero correspondiente al mes: "))
    dia = int(input("Ingrese un dia: "))
    print("Faltan tantos dias para fin de mes: ",dias_faltantes_mes(año,mes,dia))
  if ingreso == 5:
    año= int(input("Ingrese un año: "))
    mes= int(input("Ingrese el numero correspondiente al mes: "))
    dia = int(input("Ingrese un dia: "))
    print("Faltan tantos dias para fin de año: ",dias_faltantes_año(año,mes,dia))
  if ingreso == 6:
    año= int(input("Ingrese un año: "))
    mes= int(input("Ingrese el numero correspondiente al mes: "))
    dia = int(input("Ingrese un dia: "))
    print("Los dias transcurridos son: " ,dias_transcurridos(dia))
  if ingreso == 7:
    año1= int(input("Ingrese un año: "))
    mes1= int(input("Ingrese el numero correspondiente al mes: "))
    dia1= int(input("Ingrese un dia: "))
    #Ingreso los datos de la otra fecha
    año2= int(input("Ingrese otro año: "))
    mes2= int(input("Ingrese el numero correspondiente al otro mes: "))
    dia2= int(input("Ingrese otro dia: "))
    print("El tiempo transcurrido entre ambas es: ",tiempo_dosfechas(dia1,mes1,año1,dia2,mes2,año2))
  else:
    print("Saliendo del sistema")