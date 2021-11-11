#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla “la division <n> entre <m> da un cociente <c> y un resto <r>” donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

num1= int(input("Ingrese el primer numero entero:"))

num2= int(input("Ingrese el segundo numero entero:"))
#INT-> tipo de dato que permite representar números enteros dentro de una variable

cociente= int(num1 / num2)
#El cociente es el resultado de nuestra division 

resto= num1 % num2
#El resto es el numero que queda cuando la división no es exacta, para eso utilizaremos el operador "%"

print("La division" ,num1, "entre" ,num2, "da un cociente" ,cociente, "y un resto" ,resto)

