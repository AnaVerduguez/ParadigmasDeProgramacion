#Modificar el programa anterior para que pueda generar fichas de un juego quo que puede tener números de 0 a n

n= int(input("Ingrese hasta que numero de fichas desea correr el juego:"))

#En este caso le pedimos al usuario que ingrese por teclado hasta que numero de fichas desea correr
#Utilizamos la misma formula solo que en este caso se le agrega un +1 para que permita correr hasta la ultima ficha, es decir a la ultima ficha se la incluye
for i in range(0,n + 1):
  for j in range(0,n + 1):
    print(i,"|" ,j)
