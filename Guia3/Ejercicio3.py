#3)Dados 50 números enteros, informar el promedio de los mayores que 100 y la suma de los menores que –10.

#Debo tener cuidado y debo inicializar mis variables en 0 al principio del ejercicio
cantidad_numeros= 0
contador=0
suma=0
suma_menores= 0

#Mientras la cantidad de numeros que se ingresa sea menor que 50, la estructura de repeticion sigue funcionando. Una vez que se termina de ingresar todos los numeros se termina el ejercicio
while cantidad_numeros < 50:
 numeros= int(input("Ingrese un numero entero:"))
 
 if numeros > 100:
   suma= suma + numeros
   contador= contador + 1
 elif numeros < -10:
   suma_menores= suma_menores + numeros

promedio_mayores= suma / contador

print("El promedio de los mayores que 100 es: " ,promedio_mayores)
print("La suma de los menores que -10 es: " ,suma_menores)
   
 