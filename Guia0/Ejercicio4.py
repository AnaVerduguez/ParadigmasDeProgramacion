#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla “<nombre> tiene <n> letras”, donde <nombre> es el nombre de usuario en mayúsculas y <n> es el número de letras que tiene el nombre.

nombre= input("¿Cual es su nombre?:").upper()
#La funcion upper() nos permite convertir en mayuscula lo que nosotros ingresemos en la variable nombre

letras= len(nombre)
#La funcion len() nos permite saber la cantidad de letras que tiene nuestra variable nombre

print(nombre , "tiene" ,letras , "letras") 