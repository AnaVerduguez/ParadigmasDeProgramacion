#Escribir una función que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: 
# F=9/5C+32

grados_fahrenheit= float(input("Ingrese los grados Fahrenheit: "))

formula= ((grados_fahrenheit - 32) * 5/9)

print(grados_fahrenheit ,"grados Fahrenheit equivalen a" ,formula ,"grados Celsius")

