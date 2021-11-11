#Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar es: *FOTO*

cantidad_pesos= float(input("Ingrese la cantidad de pesos:"))
tasa_interes= float(input("Ingrese la tasa de interes:"))
numero_años= float(input("Ingrese los años:"))

#Usamos la funcion round() que nos permite redondear el resultado
ecuacion= round((cantidad_pesos * (1 + (tasa_interes / 100))**numero_años) ,2)

print("El monto final es: " ,ecuacion)

