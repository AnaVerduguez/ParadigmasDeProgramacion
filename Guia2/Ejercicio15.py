#15)Escribir un programa que reciba como entrada un entero representando un año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en números romanos. 

#Inicializo mis variables a utilizar
año_entero= 0
romano= ""

#Pido el año a convertir que sea ingresado por teclado
año_entero= int(input("Ingrese un año para ser transformado en numeros romano:"))

#De manera logica tratamos de descoponer a las unidades, decenas, centenas y millar para entender el proceso por el cual estan armadas y la posicion que lleva cada una

millar = (int(año_entero/1000))*1000
centena = int((año_entero-millar)/100)*100
decena = int ((año_entero- millar-centena)/10)*10
unidad = int((año_entero- millar -centena - decena))

#La unica forma que se me ocurrio para hacer la conversion fue usar las unidades,decenas, centenas y millar e irlas descomponiendolas y reemplazando por los numeros romanos

#Estructura para las UNIDADES(1)
if unidad == 1:
  romano= romano + "I"
elif unidad == 2:
  romano= romano + "II"
elif unidad == 3:
 romano= romano + "III"
elif unidad == 4:
  romano= romano + "IV"
elif unidad == 5:
  romano= romano + "V"
elif unidad == 6:
  romano= romano + "VI"
elif unidad == 7:
  romano= romano + "VII"
elif unidad == 8:
  romano= romano + "VIII"
elif unidad == 9:
  romano= romano + "IX"

#Estructura para las DECENAS(10)
if decena == 10:
  romano= romano + "X"
elif decena == 20:
  romano= romano + "XX"
elif decena == 30:
  romano= romano + "XXX"
elif decena == 40:
  romano= romano + "XL"
elif decena == 50:
  romano= romano + "L"
elif decena == 60:
  romano= romano + "LX"
elif decena == 70:
  romano= romano + "LXX"
elif decena == 80:
  romano= romano + "LXXx"
elif decena == 90:
  romano= romano + "XC"

#Estructura para las CENTENAS(100)
if centena == 100:
  romano= romano + "C"
elif centena == 200:
  romano= romano + "CC"
elif centena == 300:
  romano= romano + "CCC"
elif centena == 400:
  romano= romano + "CD"
elif centena == 500:
  romano= romano + "D"
elif centena == 600:
  romano= romano + "DC"
elif centena == 700:
  romano= romano + "DCC"
elif centena == 800:
  romano= romano + "DCCC"
elif centena == 900:
  romano= romano + "CM"

#Estructura para el MILLAR(100)
if millar == 3000:
  romano = romano + "MMM"
elif millar == 2000:
  romano = romano + "MM"
elif millar == 100:
  romano= romano + "M"

print("El numero romano de ",año_entero ,"es:" ,romano)

