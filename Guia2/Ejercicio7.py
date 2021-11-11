#7)Dado un triángulo representado por sus lados L1, L2, L3, determinar e imprimir una leyenda según sea: equilátero, isósceles o escálenos.

#Le pide al usuario que ingre por teclado el valor de los 3 lados del triangulo
lado1= int(input("Ingrese el lado 1:"))
lado2= int(input("Ingrese el lado 2:"))
lado3= int(input("Ingrese el lado 3:"))

#Equilatero -> Tiene todos sus lados iguales
#Isosceles -> Tiene dos lados iguales
#Escaleno -> Ningun lado es igual

if lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
  print("El triangulo es equilatero")
elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print("El triangulo es escaleno") 
if lado1 == lado2 and lado2 != lado3 or lado1 == lado3 and lado3 != lado2 or lado2 == lado3 and lado3 != lado1:
    print("El triangulo es isosceles")
