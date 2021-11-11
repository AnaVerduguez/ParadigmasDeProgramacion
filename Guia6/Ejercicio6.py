#6)Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

#Pimero creamos dos litas, una con los meses del año, y otra con los dias de cada mes, luego utilizamos un def
meses_año= []
dias_mes= []

def fechas(d,m):  
  meses_año=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

  dias_mes=[31,28,31,30,31,30,31,31,30,31,30,31]

#Pedimos que el usuario ingrse el numero perteneciente al mes.

  numero_mes= int(input("Ingrese un numero correspondiente a su mes para saber cuantos dias tiene:"))

#Imprimimos por pantalla
  print("El mes {0} tiene un total de {1} dias".format(meses_año[numero_mes],dias_mes[numero_mes]))

  return fechas
print(fechas(meses_año,dias_mes))
