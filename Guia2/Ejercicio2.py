#2)Dado el siguiente enunciado y su representación gráfica especifique los datos de entrada, de salida, estrategia, seguimiento y codificación. 
#Enunciado: Dado un número real que representa el importe de una compra informar las posibles formas de pago, según la siguiente tabla:
# 1 cuota  de $................. 
# 2 cuotas de $................. total #$................. (   5% de recargo)
# 6 cuotas de $................. total
# $................. ( 40% de recargo)

#Pido al usuario que ingrese el importe de su compra
importe_compra= float(input("Ingrese el importe de la compra:"))

#Recargos de las cuotas 2 y 6
#5/100= 0.05 
#40/100= 0.4
recargo_2cuotas= 0.05 
recargo_6cuotas= 0.4

#Utilizo la funcion round() que nos permite redondear los resultados
#Asi nos queda el valor de cada cuota y el total con su respectivo recargo
dos_cuotas= round(((importe_compra*recargo_2cuotas)+ importe_compra)/2)

dos_cuotas_total= round(((importe_compra*recargo_2cuotas)+ importe_compra))

seis_cuotas= round(((importe_compra*recargo_6cuotas)+ importe_compra)/6)

seis_cuotas_total= round(((importe_compra*recargo_6cuotas)+ importe_compra))

#Imprimo por pantalla las forma de pago
print("Las formas de pago son las siguientes:")
print("1) 1 cuota de $:" ,round(importe_compra) ,"(Sin recargo)")
print("2) 2 cuotas de :$" ,dos_cuotas ,"total:$" ,dos_cuotas_total , "(5% de recargo)")
print("3) 6 cuotas de :$" ,seis_cuotas  ,"total:$" ,seis_cuotas_total ,"(40% de recargo)")