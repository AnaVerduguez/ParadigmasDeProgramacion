#6)Dadas dos fechas informar cual es la más reciente. Determine cuales serían los datos de entrada y las leyendas a informar de acuerdo al proceso solicitado.

#Le pido al usuario que ingrese dia,mes y año de una fecha
dia_fecha1= int(input("Ingrese un dia en numeros:"))
mes_fecha1= int(input("Ingrese un mes en numeros:"))
año_fecha1= int(input("Ingrese un año en numeros:"))

#Le pido al usuario que ingrese dia,mes y año de otra fecha distinta a la primera
dia_fecha2= int(input("Ingrese otro dia en numeros:"))
mes_fecha2= int(input("Ingrese otro mes en numeros:"))
año_fecha2= int(input("Ingrese otro año en numeros:"))

#Aplico la misma operacion que en el ejercicio 3
fecha1=(año_fecha1*10000) + (mes_fecha1*100) + (dia_fecha1)

fecha2=(año_fecha2*10000) + (mes_fecha2*100) + (dia_fecha2)

#Si la fecha 1 es mayor que la fecha dos se imprime por pantalla que la primera fecha es la mas reciente,caso contrario la segunda fecha es la mas reciente
if fecha1 > fecha2:
  print("La primer fecha es la mas reciente")
else:
  print("La segunda fecha es la mas reciente")

