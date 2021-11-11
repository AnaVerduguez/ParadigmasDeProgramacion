#2)Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

import copy
#Primero debo de crear un def que me guarde mi lista original ingresada por teclado
def lista():
  lista_teclado= []

#Aplico un for i in range para ingresar solamente 5 valores.
#Utilizamos los metods append(agregar elementos a una lista) y los metodos deepcopy y reverse(copiar los valores anteriores e invertirlos)
  print("Ingrese 5 numeros para guardarlos en una lista y luego imprimir su inversa ")
  for i in range(5):
   lista_teclado.append(input("Ingrese un numero:"))

  lista_invertida= copy.deepcopy(lista_teclado)
  lista_invertida.reverse()

  print(lista_invertida)

lista()
