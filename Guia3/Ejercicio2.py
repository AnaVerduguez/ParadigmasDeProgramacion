#2)Dados N y M números naturales, informar su producto por sumas sucesivas.

#Diferencia: 
#Producto= 4*3
#Suma susesiva= 4+4+4

#Le pedimos al usuario que ingrese dos numeros naturales
n=int(input("Ingrese un numero natural:"))
m=int(input("Ingrese otro numero natural:"))

#El numero m nos permite identicar cuantas veces se sumara al numero, el numero n hace referencia al valor que tomara el numero para luego ser sumado
suma_sucesiva= 0

for i in range(m):
 suma_sucesiva= suma_sucesiva+n

print("El producto por sumas sucesivas es:" ,suma_sucesiva)