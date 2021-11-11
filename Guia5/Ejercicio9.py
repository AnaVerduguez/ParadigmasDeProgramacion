#9)Desarrollar un procedimiento tal que dada una hora (HHMMSS) y un tiempo también en formato HHMMSS devuelva la nueva hora que surge de sumar el tiempo a la hora  inicial, considere también si cambió el día.

#Creo mi funcion que me permita sumar la hora actual con otra hora diferente y asi obtener una hora nueva
def sumar_horas(actual,hora):
  sumar_horas=datetime.timedelta(hours=hora)
  suma= actual + sumar_horas
  return suma

#Utilizo la función estandar strftime para saber la hora actual
import datetime
hora_primera= datetime.datetime.now()
hora_nueva= int(input("Ingrese la nueva hora en formato hhmmss:"))

resultado= sumar_horas(hora_primera,hora_nueva)

print("La nueva hora sera: {0}".format(resultado))