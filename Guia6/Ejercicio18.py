#18 Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
#•	Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
#•	Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
#•	Eliminar: Me pide una cadena, y la elimina de la lista.
#•	Mostrar: Muestra la lista de cadenas
#•	Terminar

#Primero debo de crear mi lista
lista= []

#Luego creo mis variables
cadena= 0
opcion= 0
modificar1=0
modificar2=0

#La cadenas  o strings son un tipo inmutable que permite almacenar secuencias de caracteres
print("En caso de que quiera dejar de ingresar debe poner f")
cadena= input("Ingrese la cadena: ")

#aplico un while para validar lo que dije anteriormente
while cadena != "f":
  lista.append(cadena)
  cadena=input("Ingrese la cadena: ")

#Aplico un menu para realizar las operaciones de la lista
while True:
  print(""""
   BIENVENIDO AL MENU
   Elija la opcion que desee:
    1)Contar
    2)Modificar
    3)Eliminar
    4)Mostrar
    5)Terminar
    """)
  opcion= int(input("Ingrese una opcion del 1 al 5:"))

  #En caso de que el usuario elija opciones del 1 al 4 se realizan las siguiente operaciones
  if opcion == 1:
    modificar1=input("Introduzca la cadena que busca:")
    print("La cadena aparece {0} veces".format(lista.count(cadena)))
  if opcion == 2:
    modificar1=input("Introduzca la cadena que busca: ")
    modificar2=input("Introduce cadena a modificar: ")
    indice=0
    for i in lista:
      if i == modificar1:
       lista[indice]=modificar2
      i= i +1
  if opcion == 3:
    modificar1= input("Introduzca la cadena para eliminar: ")
    if modificar1 in lista:
      lista.remove(modificar1)
  if opcion == 4:
    for i in lista:
      print(i," ",end="")
  #En caso de que se ingrese el 5 se termina el programa
  if opcion == 5:
    break
  #En caso de que se ingrese otra opcion diferete se muestra un cartel
  else:
    print("Ingrese una opcion correcta")