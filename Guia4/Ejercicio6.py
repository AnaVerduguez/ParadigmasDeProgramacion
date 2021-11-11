#6)Dada una serie de M pares {color, número} que corresponden a los tiros de una ruleta. Se pide informar:
#a)	cuántas veces salió el número cero y el número anterior a cada cero
#b)	cuántas  veces seguidas llegó a repetirse el color negro
#c)	cuántas  veces seguidas llegó a repetirse el mismo número y cuál fue
#d)	el mayor número de veces seguidas que salieron alternados el rojo y el negro
#e)	el mayor número de veces seguidas que se negó la segunda docenas

#Defino mis variables

numero= int
color= str
programa= True
contador_cero= 0
numero_anterior= -1

color_anterior= ""
contador_negro= 0

numero_repetido= 0
contador_repetido=0

alternacion= 0
max_alternacion= 0

negacion_docenas=0
max_docenas= 0

print("BIENVENIDO A LA RULETA")
print("En la ruleta existen 3 colores, el rojo el negro y el verde. del 1 al 32 varian entre rojos y negros y el cero es verde.")
print("Para finalizar la carga de numeros ingrese un numero negativo")

while programa == True:
  #Pido al usuario que ingrese el numero del tiro
  numero= int(input("Ingrese el numero del tiro de la ruleta:"))
  #Valido que el numero sea correcto y a su vez le pido al usuario el color de dicho numero
  if numero >= 0:
    color= input("Ingrese el color que corresponde al numero:").upper()

    #a)Cuantas veces salio cero y el num anterior.
    #En caso de que el numero sea 0, se suma en una variable contador_cero
    if numero == 0:
      contador_cero = contador_cero + 1
      print("El numero 0 se repitio {0} vez en el juego".format(contador_cero))
    #Para saber cual fue el numero del tiro anterior solo debemos utilizar el operador mayor
      if numero_anterior >= 0:
        print("El numero anterior a 0 es: {0}".format(numero_anterior))

    #b)Cuantas veces se repitio el color negro
    #Para esto debemos crear un nuevo contador en donde sumemos los colores anteriores y el nuevo
    if color_anterior == "NEGRO" and color == "NEGRO":
      contador_negro= contador_negro + 1
    
    #c)Cuantas veces seguidas se repitio el mismo numero y cual es
    #Para esto debemos crear un contador en donde sumemos las veces que se repite el mismo numero. 
    if numero_anterior == numero:
      contador_repetido= contador_repetido + 1
    
    #d)Mayor numero de veces seguidas que salieron alternados el rojo y el negro
    #En este caso tambien debo crear un nuevo contador que me permita guardar las veces que rojo y negro se alternan. Luego de eso aplico la formula de maximos
    if color == "NEGRO" and color_anterior == "ROJO" or color == "ROJO" and color_anterior == "NEGRO":
      alternacion= alternacion + 1

      if alternacion > max_alternacion:
        max_alternacion = alternacion
    
    #c)Mayor número de veces seguidas que se negó la segunda docena
    # 2da docena -> desde el 13 hasta el 25. Debemos de aplicar un contador y luego un maximo
    if numero >=13 and numero <=25:
      negacion_docenas= negacion_docenas + 1

      if negacion_docenas > max_docenas:
        max_docenas = negacion_docenas
  
    #A numero anterior y color anterior le asigno el valor de numero y color que me ayuda a saber el numero y el color que hubo anteriormete
    numero_anterior = numero
    color_anterior = color
  else:
  #Si el numero es negativo entonces se imprime por pantalla los resultados
    print("b)Veces seguidas llegó a repetirse el color negro {0}".format(contador_negro))
    print("c)Veces seguidas llegó a repetirse el mismo numero {0} y fue {1}".format(contador_repetido, numero_anterior))
    print("d)Mayor numero de veces seguidas que salieron alternados el rojo y el negro {0}".format(max_alternacion))
    print("e)Mayor número de veces seguidas que se nego la segunda docena {0}". format(max_docenas)) 

    print("Fin del programa")
    programa= False


      

