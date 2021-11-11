#1)Desarrollar una función que calcule el máximo común divisor de dos números enteros A, B con el siguiente algoritmo:
#a)Dividir A por B, y calcular el resto (0 < R < B)
#b)Si R = 0, el MCD es B, si no seguir en 3)
#c)Reemplazar A por B, B por R, y volver al paso 1)

#MCD -> Es el mayor numero por el cual se pueden dividir dos o mas numeros, sin dejar ningun residuo

#Le pido al usuario dos valores
valor_a= int(input("Ingrese el valor de a:"))
valor_b= int(input("Ingrese el valor de b:"))

#Creo mi funcion utilizando mis variables a y b
#valor_a y valor_b son los parametro de mi funcion
def maximo_comun_divisor(a,b):
  #a)Divido a por b y calculo el resto
  resto = -1
  #El resto debe valer distinto que 0 para entrar al while
  while resto != 0:
    resto = a % b
    #b)Si el resto es 0, el MCD es b y finalizo mi funcion
    #return -> Final de una funcion
    if resto == 0:
      return b
    #c)Si el resto no es 0 entonces remplazo a por b y b por resto
    else:
      a = b
      b = resto

resultado = maximo_comun_divisor(valor_a,valor_b)
print("El maximo comun divisor es: {0}".format(resultado))