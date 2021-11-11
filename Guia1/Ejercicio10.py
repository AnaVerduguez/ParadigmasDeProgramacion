#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

numero1= int(input("Ingrese el primer numero: "))
numero2= int(input("Ingrese el segundo numero: "))

print("Los numeros pares entre" ,numero1 ,"y" ,numero2 ,"son:")

#Toma los parametros entre el numero1 y el numero2
for i in range(numero1,numero2):
  #Utilizo la funcion IF para averiguar los numeros pares entre numero1 y numero2. En caso de que se cumpla el IF se imprime los numeros pares.
  if (i % 2 == 0):
   print(i)



