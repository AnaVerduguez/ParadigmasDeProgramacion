#A partir de un valor entero ingresado por teclado, se pide informar:
#La quinta parte de dicho valor
#El resto de la división por 5
#La séptima parte del resultado del punto a)

#Le pido al usuario que ingrese un valor entero por teclado
valor_entero= int(input("Ingrese un valor entero:"))

#Quinta parte
quinta_parte= round(valor_entero / 6)

#Resto de la division por 5
resto= round(valor_entero % 5)

#Septima parte del resultado del punto a
septima_parte= round(quinta_parte / 7)

#Muestro por pantalla los resultados de mis operaciones realizadas
print("La quinta parte de dicho valor es:" ,quinta_parte)
print("El resto de la división por 5 es:" ,resto)
print("La séptima parte del resultado del punto a) es:" ,septima_parte)

