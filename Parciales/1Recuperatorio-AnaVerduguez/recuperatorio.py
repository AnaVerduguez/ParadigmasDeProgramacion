#1)Se reciben los vendedores de tres sucursales.Los vendedores tienen el codigo de sucursal reciben un sueldo base, mas un 10% extra por comisiones de sus ventas.
#a)Cada vendedor desea saber cuanto dinero obtendra por concepto de comisiones por las tres ventas que realizo en el mes.
#b)El total que recibira en el mes tomando en cuenta su sueldo base y sus comisiones
#c)Se desea saber cual es la sucursal con mas ventas.
#Realizar un menu de opciones y ademas una opcion que indique la salida del programa.
#El codigo debera ser comentado indicando la logica de la solucion y debera estar cargado en repl.it

#Defino las variables que voy a utilizar para realizar las operaciones
#Defino el codigo que tendra cada una de las 3 sucursales,esto me sirve para identificar a cada una
#Definimos que el sueldo base de cada trabajador es 25000,ademas de eso le agregamos la comision por ventas correspondientes en otra variable
sucursal_1= 1234
sucursal_2= 1235
sucursal_3= 1236

sueldo_base= 25000

contador1=0
contador2=0
contador3=0

venta_mayor= 0
sucursal_mayor=0

menu= ""
opcion= 0

#Le pido al usuario que ingrese los datos que necesito para realizar las operaciones


print("¡BIENVENIDO!")
print("Codigo SUCURSAL 1= 1234")
print("Codigo SUCURSAL 2= 1235")
print("Codigo SUCURSAL 3= 1236")

codigo_sucursal=int(input("Ingrese el codigo de sucursal:"))

#La ventas solo deben ser 3 por mes por cada vendedor para entrar al bucle
for i in range(1,3+1):

  if (codigo_sucursal==1234):
    venta1=int(input("Ingrese la venta"))
    venta_1sucursal= venta1+ (venta1*0.10)
    contador1= contador1+1

  elif (codigo_sucursal==1235):
    venta2=int(input("ingrese la venta"))
    venta_2sucursal= venta2+ (venta2*0.10)
    contador2= contador2+1

  elif (codigo_sucursal==1236):
    venta3=int(input("ingrese la venta"))
    venta_3sucursal= venta3+ (venta3*0.10)
    contador3= contador3+1  

  else: 
    print("Ingrese un codigo de sucursal correcto")

#El total que recibira en el mes 
if (codigo_sucursal ==1234):
  total_dinero1= sueldo_base + contador1
if (codigo_sucursal ==1235):
  total_dinero2=  sueldo_base + contador2
if (codigo_sucursal ==1236):
  total_dinero3=  sueldo_base + contador3

#Sucursal con mas ventas

if venta_mayor == 0:
  venta_mayor = contador1

if venta_mayor > contador2:
  venta_mayor = contador2

if venta_mayor > contador3:
  venta_mayor = contador3 

#Utilizo un menu de opciones para que el usuario elija la opcion que desee y asi le muestre los resultados por pantalla. En caso de que el usuario ingrese "SI" el menu finaliza
while (menu != "SI"):
  print("MENU DE OPCIONES:")
  print("1)Dinero que obtendra cada vendedor por concepto de comisiones por las tres ventas que realizo en el mes(ingrese la sucursal):")
  print("2)Total que recibira cada vendedor en el mes tomando en cuenta su sueldo base y sus comisiones(ingrese la sucursal:")
  print("3)Sucursal con mas ventas:")

  opcion= int(input("Ingrese la opcion que desee:"))

  if (opcion==1):
    print("El dinero que obtendra cada vendedor por concepto de comisiones por las tres ventas que realizo en el mes es: {0}").format()
  
  elif (opcion==2):
    print("El total que recibira cada vendedor en el mes tomando en cuenta su sueldo base y sus comisiones es: {0}").format()
    
  elif (opcion==3):
    print("La sucursal con mas ventas es: {0}").format()

  else:
    print("Ingrese una opcion correcta")
  
  menu=input("Desea finalizar el menu?SI/NO:").upper()
