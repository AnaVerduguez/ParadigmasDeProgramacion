#14)Suponiendo que el primer día del año fue lunes, escribir un programa que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo: si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'. 

#Le pido al usuario que ingrese el numero del dia que prefiera
dia=int(input("Ingrese el numero del dia que quiera del 1 al 366:"))

#Para obtener que dia de la semana devuelve el numero debemos calcular el resto de la division por 7 -> dias de las semana
resto= dia%7

#Dependiendo del resto sabremos calcular a que dia pertenece
if resto == 1:
  print("El dia es Lunes")
elif resto == 2:
  print("El dia es Martes")
elif resto == 3:
  print("El dia es Miercoles")
elif resto == 4:
  print("El dia es Jueves")
elif resto == 5:
  print("El dia es Viernes")
elif resto == 6:
  print("El dia es Sabado")
elif resto == 7:
  print("El dia es Domingo")