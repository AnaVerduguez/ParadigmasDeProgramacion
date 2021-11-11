#Escribir un programa que le pregunte al usuario un número n e imprima los primeros n números triangulares, junto con su índice. Los números triangulares se obtienen mediante la suma de los números naturales desde 1 hasta n. Es decir, si se piden los primeros 5 números triangulares, el programa debe imprimir:
#1 - 1 
#2 - 3 
#3 - 6 
#4 - 10 
#5 - 15 

numero_triangular= int(input("Ingrese un numero para luego imprimir sus numeros triangulares:"))
#Toma los parametros entre el 1 y el numero ingresado por teclado
#El +1 nos permite agregar el ultimo numero triangular a nuestro bucle
#Volvemos a utilizar round para redondear el resultado
print("Usando la ecuacion:")
for i in range(1, numero_triangular + 1):
  i = round(i * ( i + 1 ) / 2 )
  print(i)

print("Sin usar la ecuacion:")
for i in range(1, numero_triangular + 1):
  numero_triangular= i + numero_triangular
  print(numero_triangular)

#Se realiza mas operaciones cuando usamos la ecuacion, ya que utilizamos la multiplicacion, la suma y la division. 


