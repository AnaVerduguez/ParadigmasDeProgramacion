#12)Escribir un algoritmo, que devuelva el valor absoluto de cualquier valor que reciba

#Pido al usuario que ingrese un valor por teclado
valor= int(input("Ingrese un valor:"))

#El valor absoluto de un numero positivo es el mismo número, y el valor absoluto de un número negativo es su opuesto(esto lo podemos lograr multiplicando el numero por -1)
if valor > 0:
  print ("El valor absoluto de" ,valor ,"es" ,valor)
elif valor < 0:
 print ("El valor absoluto de" ,valor ,"es" ,(valor*(-1)))
