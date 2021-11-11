#Escribir un programa que pregunte al usuario: a) su nombre, y luego lo salude. b) dos números, y luego muestre el producto. 

#A)Pedir nombre y que se lo salude
nombre= input("¿Cual es su nombre?")

print ("¡Hola" ,nombre ,"bienvenidx!")

#B)Producto entre dos numeros
numero1= int(input("Ingrese el primer numero para multiplicar:"))

numero2= int(input("Ingrese el segundo numero para multiplicar:"))

producto= numero1*numero2

print("El producto de" ,numero1 ,"y" ,numero2 ,"es" ,producto)