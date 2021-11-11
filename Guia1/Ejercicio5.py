#Implementar algoritmos que resuelvan los siguientes problemas: a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos. b) Dado un número entero n, imprimir su tabla de multiplicar.

#Suma,resta,division y multiplicacion de dos numeros
numero1= int(input("Ingrese el primer numero:"))
numero2= int(input("Ingrese el segundo numero:"))

suma= numero1 + numero2
resta= numero1 - numero2
division= numero1 / numero2
multiplicacion= numero1 * numero2

print("1.La suma entre" ,numero1 ,"y" ,numero2 ,"es:" ,suma)
print("2.La resta entre" ,numero1 ,"y" ,numero2 ,"es:" ,resta)
print("3.La division entre" ,numero1 ,"y" ,numero2 ,"es:" ,division)
print("4.La multiplicacion entre" ,numero1 ,"y" ,numero2 ,"es:" ,multiplicacion)

#Tabla de multiplicar de un numero entero
numero_entero= int(input("Ingrese un numero entero para luego mostrar su tabla de multiplicar:"))

for i in range (11):
 print (numero_entero * i)