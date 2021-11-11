#16. Vamos a crear un programa que tenga el siguiente menú:
#1.	Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
#2.	Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
#3.	Longitud de la lista: te muestra el número de elementos de la lista.
#4.	Eliminar el último número: Muestra el último número de la lista y lo borra.
#5.	Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
#6.	Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
#7.	Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
#8.	Mostrar números: Muestra los números de la lista
#9.	Salir

#Comenzamos definiendo la variable para mi menu y mi lista
numeros= []
ingreso= 0
continuar= bool(True)

#Imprimo por pantalla el menu que me muestra las opciones
while continuar == True:
    print("""
    BIEVENIDO AL MENU
    Elija la opcion que desea hacer en la lista:
    1)Añadir un numero a la lista
    2)Añadir un numero a la lista en una posicion
    3)Longitud de la lista
    4)Eliminar el ultimo numero
    5)Eliminar un numero
    6)Contar numeros
    7)Posiciones de un numero
    8)Mostrar numeros
    9)Salir del programa
    """)

    ingreso= int(input("Ingrese la opcion: "))
    #En caso de que se ingrese 9 el programa finaliza
    if ingreso == 9:
      continuar = False
    #En caso de que se ingrese cualquier num del 1 al 8 se van realizando las operacion correspondientes, utilizo los metodos de python que conozco
    if ingreso == 1:
      numeros.append(int(input("Ingrese un numero: ")))
    if ingreso == 2:
      posicion = int(input("Ingrese posicion: "))
      num_nuevo = int(input("Ingrese el numero: "))
      numeros.insert(posicion, num_nuevo)
      print(numeros)
    if ingreso == 3:
      print("La longitud es: {0}".format(len(numeros)))
    if ingreso == 4:
      numeros.pop()
      print("La lista eliminando el ultimo numero queda: {0}".format(numeros)
    if ingreso == 5:
      valor = int(input("Ingrese la posicion del numero que quiere eliminar: "))
      numeros.pop(valor)
      print ("La lista eliminando ese numero queda: {0}".format(numeros))
    if ingreso == 6:
      contar = input("Ingrese el numero: ")
      print("La cantidad de veces que aparece es:{0} ".format(numeros.count(contar))) 
    if ingreso == 7:
      numero = int(input("Ingrese el numero: "))
      print ("Esta en la posición: {0}".format(numeros.index(numero))) 
    if ingreso == 8:
      print("Los numeros son: {0}".format(numeros))
else:
  print ("Saliendo del programa")
    




