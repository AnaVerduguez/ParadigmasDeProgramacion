#7)Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

#Debo crear 3 listas

lista1= []
lista2= []
lista3= []

#Aplicamos un for i in range del 1,6 ya que solo debo tener 5 entero por cada lista. Luego le sumamos los numeros ingresados
for i in range (1,6):
  lista1.append(int(input("Ingrese un numero entero para la primera lista:")))

#Hacemos lo mismo para la lista 2
for i in range (1,6):
  lista2.append(int(input("Ingrese un numero entero para la segunda lista:")))

#Por ultimo sumamos todo en la lista 3
lista3= lista1 + lista2

#Muestro por pantalla lo que contiene mi lista 3, es decir el resultado de mis operacion

print(lista3)