#2)Suponiendo que el primer día del año fue lunes, escribir una función que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo: si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'

#Defino mis variables que usare
numero= 0
dia= 0

#Creo mi funcion
def dias(numero,dia):
  numero=int(input("Ingrese el día del año que desee: "))
  #Valido que el numero ingresado pertenezca a un dia del año
  if numero >=1 and numero <= 366:
    #Aplico un ciclo que me permite saber a que dia de la semana pertenece
    for i in range(numero):
      dia= dia + 1
      if dia >= 8:
        dia= dia - 8
        dia= dia + 1
  if dia == 1:
    print ("Es lunes")
  elif dia == 2:
    print ("Es martes")
  elif dia == 3:
    print ("Es miercoles")
  elif dia == 4:
    print ("Es jueves.")
  elif dia == 5:
    print ("Es viernes")
  elif dia == 6:
    print ("Es sabado")
  else:
    print ("Es domingo.")
  return 

dias(numero,dia)


