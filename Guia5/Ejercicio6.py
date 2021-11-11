#6)Desarrollar un procedimiento que imprima una fecha en formato DD/MM/AA. El dato que recibe es un longint con una fecha en formato aaaammdd.

#fecha lo debo declarar como un string para manipular la lista
fecha_ingresada= input("Ingrese la fecha en formato aaaammdd:")

def formato_ddmmaa(fecha):
  dia=fecha[6:8]
  mes=fecha[4:6]
  año=fecha[2:4]

  print("La fecha en dormato dd/mm/aa es {0}/{1}/{2}".format(dia,mes,año))

formato_ddmmaa(fecha_ingresada)