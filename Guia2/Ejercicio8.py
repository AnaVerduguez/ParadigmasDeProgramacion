#8)Dados un mes y el año correspondiente informar cuantos días tiene el mes.

año= int(input("Ingrese un año:"))
mes= int(input("Ingrese un mes en numeros del 1 al 12:"))

#Cada cuatro años se añade un dia mas al mes de febrero,es por eso que cualquier año divisible por 4 es un año bisiesto
año_bisiesto= año % 4

if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12: 
 print("El mes tiene 31 dias")
elif mes==4 or mes==6 or mes==9 or mes==11:
 print("El mes tiene 30 dias")
elif mes==2:
 if año_bisiesto != 0:
   print ("El mes tiene 28 dias")
 elif año_bisiesto == 0:
   print ("El mes tiene 29 dias")
  



