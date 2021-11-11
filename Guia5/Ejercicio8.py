#8)Desarrollar una rutina tal que dada una fecha (AAAAMMDD) y un número natural que representa una cantidad de días, calcule y retorne la nueva fecha en tres parámetros  año (AAAA), mes (MM) y día (DD) que resulte de incrementar al parámetro fecha con el parámetro cantidad de días. 

import datetime
#Creo mi funcion que me permite sumar los dias a la fecha actual y asi obtener la fecha nueva
def sumar_dias(actual,dias):
  sumar_dias= datetime.timedelta(days=dias)
  suma=actual + sumar_dias
  return suma

#Utilizo la función estandar datetime para saber la fecha actual
fecha_actual= datetime.date.today()
numero_ingresado= int(input("Ingrese la cantidad de dias:"))

while numero_ingresado <=0 or numero_ingresado >31:
  break

resultado= sumar_dias(fecha_actual,numero_ingresado)
print("La nueva fecha es: {0}".format(resultado))


