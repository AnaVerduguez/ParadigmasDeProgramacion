#17)Crear un programa que añada números a una lista hasta que introducimos un número negativo. A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

#Primero creo mis lista y mi variable numero
lista= []
lista_sinduplicados= []
numero= 0

print("Si desea terminar dera ingresar un num negativo")
numero=int(input("Ingrese un numero: "))

#El numero dera de ser postiivo para ingresar a la lista, si es positivo se agrega 
while numero >=0:
  lista.append(numero)
  numero=int(input("Ingrese un numero: "))

#Creamos un for aparte para ingresar los numeros que no son duplicado
for i in lista:
  if i not in lista_sinduplicados:
    lista_sinduplicados.append(i)

#Imprimo por pantalla el resultado de mi lista
for i in lista_sinduplicados:
    print(i," ",end="")
  