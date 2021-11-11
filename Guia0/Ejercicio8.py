#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

CuentaAhorros= float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros:$"))

PrimerAño= round(((CuentaAhorros * 0.04) + CuentaAhorros), 2)

#0.04 -> el 4% de interés al año
#Volvemos a utilizar la funcion round() que nos permite redonder cada cantidad a dos decimales

SegundoAño= round(((PrimerAño * 0.04) + PrimerAño), 2)

TercerAño= round(((SegundoAño * 0.04) + SegundoAño), 2)
#Realizamos la misma operacion para los tres años

print("Cantidad de ahorros tras el primer año:$" ,PrimerAño)
print("Cantidad de ahorros tras el segundo año:$" ,SegundoAño)
print("Cantidad de ahorros tras el tercer año:$" ,TercerAño)