#Dada una terna de números naturales que representan al día, al mes y al año de una determinada fecha informarla como un solo número natural de 8 dígitos (AAAAMMDD).

#Pido el dia,el mes y el año por teclado
dia= int(input("Ingrese un dia en numeros:"))
mes= int(input("Ingrese una mes en numeros:"))
año= int(input("Ingrese un año en numeros:"))

#Imprimo por pantalla el resultado de lo que se pide por teclado en formato (AAAAMMDD)
#Utilizo el 10000 y el 100 para cambiar la posicion de los numeros
print((año*10000) + (mes*100) + (dia))