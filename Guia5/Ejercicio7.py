#7)Desarrollar una rutina tal que dados una base y un exponente, enteros positivos, calcule  y retorne la potencia.

#Debo de dintinguir los datos de entrada que ingresa el usuario y los parametros que tiene mi funcion
base_ingresada= int(input("Ingrese la base de la potencia:"))
exponente_ingresado= int(input("Ingrese el exponente de la potencia:"))

def potencias(base,exponente):
  potencia= base ** exponente
  #retorno el resultado de potencia
  return potencia

resultado= (potencias(base_ingresada, exponente_ingresado))
print("La potencia es: {0}".format(resultado))

