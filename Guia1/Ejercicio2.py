#Implementar algoritmos que permitan: a) Calcular el perímetro de un rectángulo dada su base y su altura. b) Calcular el área de un rectángulo dada su base y su altura. c) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1, x2, y1, y2. d) Calcular el perímetro de un círculo dado su radio. e) Calcular el área de un círculo dado su radio. f) Calcular el volumen de una esfera dado su radio.g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. 

#A)Perimetro de un rectangulo
base1= float(input("Ingrese la base del rectangulo: "))
altura1= float(input("Ingrese la altura del rectangulo: "))

perimetro= 2*(base1) + 2*(altura1)

print("El perimetro del rectangulo es: " ,perimetro)

#B)Area de un rectangulo
base2= float(input("Ingrese la base del rectangulo: "))
altura2= float(input("Ingrese la altura del rectangulo: "))

area= base2*altura2

print("El area del rectangulo es: " ,area)

#C)Area de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1, x2, y1, y2
x1= float(input("Ingrese el valor de la cordenada x1:"))
x2= float(input("Ingrese el valor de la cordenada x2:"))
y1= float(input("Ingrese el valor de la cordenada y1:"))
y2= float(input("Ingrese el valor de la cordenada y2:"))

area_rectangulo= (x1 + x2) * (y1 + y2)

print("El area del rectangulo es: " ,area_rectangulo)

#D)Perímetro de un círculo dado su radio
#Utilizo la funcion integrada en Python para utilizar π y √
import math
radio1= float(input("Ingrese el radio del circulo:"))
perimetro1= 2 * math.pi * radio1

print("El perimetro del circulo es: " ,perimetro)

#E)Area de un círculo dado su radio
radio2= float(input("Ingrese el radio del circulo:"))
area2= math.pi * (radio2**2)

print("El area del circulo es: " ,area)

#F)Volumen de una esfera dado su radio
radio3=float(input("Ingrese el radio de la esfera:"))
volumen= round((4/3) * math.pi * (radio3**3))

print("El volumen de la esfera es: " ,volumen)

#G)Dados los catetos de un triángulo rectángulo,calcular su hipotenusa. 
cateto1=float(input("Ingrese el primer cateto del triangulo rectangulo:")) 
cateto2=float(input("Ingrese el segundo cateto del triangulo rectangulo:"))

hipotenusa= round(math.sqrt (cateto1**2 + cateto2**2))

print("La hipotenusa del triangulo rectangulo es: " ,hipotenusa)

