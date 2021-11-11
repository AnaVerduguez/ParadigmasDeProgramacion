#6)Se ingresa un conjunto de valores reales, cada uno de los cuales representan el sueldo de un empleado, excepto el último valor que es cero e indica el fin del conjunto. Se pide desarrollar un programa que determine e informe:
#a)Cuántos empleados ganan menos $1.520.
#b)Cuántos ganan  $1.520 o más pero menos de $2.780.
#c)Cuántos ganan $2.780 o más pero menos de $5.999.
#d)Cuántos ganan $5.999 o más.

#Declaro que el sueldo vale -1 para que me permita entrar al ciclo las veces que sea necesario.Inicializo mis contador en 0 para luego utilzarlos mas adelante
sueldo= -1
contador_a=0
contador_b=0
contador_c=0
contador_d=0

#Mientras que el sueldo sea diferente a 0 entra a la estructura de repeticion. Le aviso al usuario que el programa finaliza si oprime 0, si el sueldo vale 0 finalizo el programa.
print("Si desea finalizar el programa oprima 0")
while sueldo != 0:
 sueldo= float(input("Ingrese el sueldo del empleado:"))
 if sueldo == 0:
   print("El programa finalizo")
 elif sueldo < 1520:
   contador_a= contador_a + 1
 elif sueldo >= 1520 and sueldo < 2780:
    contador_b= contador_b + 1
 elif sueldo >= 2780 and sueldo < 5999:
    contador_c=contador_c + 1
 elif sueldo >= 5999:
    contador_d=contador_d + 1

print("INFORME:") 
print("a)Empleados que ganan menos $1.520:" ,contador_a)
print("b)Empleados que ganan $1.520 o más pero menos de $2.780:" ,contador_b)
print("c)Empleados que ganan $2.780 o más pero menos de $5.999:" ,contador_c)
print("d)Empleados que ganan $5.999 o más:" ,contador_d)

