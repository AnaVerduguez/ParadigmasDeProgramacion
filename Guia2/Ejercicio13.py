#13)Escribir un algoritmo que permita encontrar:
#a) El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y c), indicando si es un máximo o un mínimo. 
#b) Las raíces (reales) de un polinomio de segundo grado. Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por cero, ni calcular la raíz de un número negativo). 
#c) La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta). Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la operación.

#a)Máximo o mínimo de un polinomio de segundo grado.
#Polinomio de segundo grado -> y= ax^2 + bx + c"

#Pedimos al usuario que ingrese por teclado los valores de los coeficientes a,b y c
import math
math.sqrt 

a= int(input("Ingrese el valor de a:"))
b= int(input("Ingrese el valor de b:"))
c= int(input("Ingrese el valor de c:"))

x= round(((b)/(2*a)))
y= round((a*(x**2)) + (b*x) + c)

if y > 0:
  print("El maximo del polinomio es:" ,(x,y))
else:
  print("El minimo del polinomio es:" ,(x,y))

#b)Raíces (reales) de un polinomio de segundo grado

#Vuelvo a utilizar las mismas variables
a= int(input("Ingrese el valor de a:"))
b= int(input("Ingrese el valor de b:"))
c= int(input("Ingrese el valor de c:"))

#Implementamos la formula resolvente

#Para hacer la formula resolvente debemos utilizar dos variables, una positiva y otra negativa
calculo= (b**2) - (4 * a * c)
raiz= (calculo)**(0.5)

raiz_pos= float(0)
raiz_neg= float(0)

raiz_pos= (-b + ((b * (-1)) - raiz) / (2 * a))

raiz_neg= (-b - ((b * (-1)) - raiz) / (2 * a))

print("Las raices son: " ,(raiz_pos,raiz_neg))
 
#c)Intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta)

#Le pido al usuario que ingrese el valor de la pendiente y ordenada de las dos rectas 
primer_pendiente= int(input("Ingrese el valor de la pendiente de la primera recta:"))
primer_ordenada= int(input("Ingrese el valor de la ordenada de la primera recta:"))

segunda_pendiente=int(input("Ingrese el valor de la pendiente de la segunda recta:"))
segunda_ordenada=int(input("Ingrese el valor de la ordenada de la segunda recta:"))

#En caso de que la primera y segunda pendiente sean diferentes se realiza la operacion del if, caso contrario se muestra por pantalla un mensaje de que no se puede
if primer_pendiente != segunda_pendiente:
  x= round((primer_ordenada - segunda_ordenada) / (segunda_pendiente - primer_pendiente))
  
  y= round((segunda_pendiente * primer_ordenada - primer_pendiente * segunda_ordenada) / (segunda_pendiente - primer_pendiente))
else:
  print("Las pendientes no deben de ser iguales")
print("La interseccion entre las rectas se da entre:" ,(x,y))