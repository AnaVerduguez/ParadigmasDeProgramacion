#4)Dada la fracción P/Q, para P y Q naturales informar la mayor cantidad de simplificaciones. Desarrolle y utilice una función que reciba dos números naturales y retorne el menor factor común. Ej: 360/60 = 180/30 = 90/15 = 30/5 = 6/1

p= int(input("Ingrese el numerador de la fraccion:"))

q= int(input("Ingrese el denominador de la fraccion:"))

#Creo una nueva funcion que me permita ingresar dor numero naturales y retornar el menor factor comun
def fraccion(numerador,denominador):
  #Aplico la funcion predeterminada de python que me permite utilizar fraccion
    from fractions import Fraction
    resultado= Fraction(p, q)
    print("El minimo factor comun es: {0}".format(resultado))
    return fraccion

print(fraccion(p,q))

 
