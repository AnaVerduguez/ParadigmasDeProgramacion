#3)Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

#Creo mi lista con las notas
notas= []

#Creo mi def con las operaciones necesarias para llevar a cabo mi ejercicio
def notas_alumno(a,b):
  for a in b:
    print("La nota media es: {0}".format(sum(b)/len(b)))
    print("La nota mas alta es: {0}".format(max(b)))
    print("La nota menor es : {0}".format(min(b)))

#Solo debemos ingresar 5 notas, para eso utilizaremos un for i in range
for i in range(1,6):
  nota= int(input("Ingrese la nota:"))

  notas.append(nota)
#Muestro por pantalla mi def
notas_alumno(nota,notas)