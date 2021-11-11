#1)Dados 10 valores informar el mayor

contador= 0
numero_mayor= 0

#Aplicamos la siguiente formula para sacar maximos. Debemos de aplicar un condicional -> IF. 
#Creamos una variable contador y otra varible numero_mayor donde se guardara el resultado final
# Igualamos a 0 la variable numero_mayor, le asignamos un valor y luego comparamos.
while contador < 10:
  numero= int(input("Ingrese un numero: "))
  if numero_mayor == 0:
    numero_mayor = numero
  elif numero > numero_mayor:
    numero_mayor = numero
  contador = contador + 1

print("El valor mas grande es {0}".format(numero_mayor))