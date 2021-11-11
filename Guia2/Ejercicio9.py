#9)Dado el siguiente enunciado, estrategia y representación gráfica especifique los datos de entrada, de salida y la codificación en Python. 
#Enunciado: Dados dos números, mostrar un menú con opciones de sumar, restar o multiplicar dichos números. Solicite elegir una opción.

#Pedimos al usuario que ingrese por teclado dos numeros
numero1= int(input("Ingrese un numero:"))
numero2= int(input("Ingrese otro numero:"))

#Mostramos por pantalla las opcion del menu y guardamos la opcion en una variable para luego utilizarla mas adelante
print("-----------M E N U------------")
print("1)Si desea sumar los dos numeros elija la opcion  1")
print("2)Si desea restar los dos numeros elija la opcion 2")
print("3)Si desea multiplicar los dos numeros elija la opcion 3")

opcion= int(input("Elija la opcion:"))

#Aplicamos los condicionales para mostrar las operaciones deseadas por pantalla.
if opcion == 1:
  print("La suma entre los dos numeros es:" ,(numero1+numero2))
elif opcion == 2:
  print("La resta entre los dos numeros es:" ,(numero1-numero2)) 
elif opcion == 3:
  print("La multiplicacion entre los dos numeros es:" ,(numero1*numero2))
else:
  print("Ingrese una opcion valida")
