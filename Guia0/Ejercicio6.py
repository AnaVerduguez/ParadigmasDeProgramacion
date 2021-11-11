#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase “Tu indice de masa corportal es <imc>” donde <imc> es el indice de masa corporal calculado redondeado con dos decimales.

peso= float(input("Ingrese su peso en kilogramos:"))

estatura= float(input("Ingrese su estatura en metros:"))

masacorporal= round((peso/estatura**2), 2)
#Masa Corporal o IMC = kg/m2

#Funcion round() que nos permite redondear los decimales que nosotros querramos utilizar, en este caso son dos decimales

print("Tu indice de masa corporal es" ,masacorporal)