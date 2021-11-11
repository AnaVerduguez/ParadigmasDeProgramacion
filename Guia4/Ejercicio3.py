#3)Dado un conjunto de Nombres y Fechas de nacimientos (AAAAMMDD), que finaliza con un Nombre = ‘FIN’, informar el nombre de la persona con mayor edad y el de la más joven.

#Me permite saber la fecha actual 
from datetime import date 

fecha_hoy = date.today()

#Inicializo las variables a utilizar
nombre= ""
fecha_nacimiento= 0
mayor_edad= 0
menor_edad= 0
nombre_mayor= ""
nombre_menor= ""

print("Debera ingresar la palabra FIN en nombre para finalizar la carga de personas")

while nombre != "FIN":
  nombre= input("Ingrese su nombre:").upper()
  
  #Aplico un break para que finalice mi programa
  if nombre == "FIN":
    break

  fecha_año= int(input("Ingrese su año de nacimiento de la siguiente forma(AAAA):"))
  fecha_mes= int(input("Ingrese su mes de nacimiento de la siguiente forma(MM):"))
  fecha_dia= int(input("Ingrese su dia de nacimiento de la siguiente forma(DD):"))
  
  #Esto me permite guardar el dia, el mes y el año en una sola variable
  fecha_nacimiento= date(int (fecha_año),int (fecha_mes),int (fecha_dia))

  if mayor_edad == 0:
    mayor_edad= fecha_nacimiento
    nombre_mayor = nombre

  if menor_edad == 0:
    menor_edad= fecha_nacimiento
    nombre_menor = nombre

#Comparo las fechas para encontrar al mayor de edad y lo asigno en la variable nombre_mayor y encuentro al menor de edad y le asigno en la variable nombre_menor

  if fecha_nacimiento < mayor_edad:
    mayor_edad = fecha_nacimiento
    nombre_mayor= nombre
  
  if fecha_nacimiento> menor_edad:
    menor_edad = fecha_nacimiento
    nombre_menor = nombre

print("La persona mas grande es {0} y el de la menor es {1}".format(nombre_mayor, nombre_menor))
