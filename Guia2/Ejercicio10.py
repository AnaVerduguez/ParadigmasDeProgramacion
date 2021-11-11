#10)Se ingresa una edad, mostrar por pantalla alguna de las siguientes leyendas:
#‘menor’ si la edad es menor o igual a 12  
#‘cadete’ si la edad está comprendida entre 13 y 18
#‘juvenil’ si la edad es mayor que 18 y no supera los 26
#‘mayor’ en el caso que no cumpla ninguna de las condiciones anteriores

#Se pide al usuario que ingrese una edad por teclado
edad= int(input("Ingrese una edad:"))

#Utilizo los condicionales if,elif y else para mostrar por pantalla las leyendas
if edad <= 12:
 print("Menor")
elif edad >= 13 and edad <= 18:
  print("Cadete")
elif edad >18 and edad <=26: 
  print("Juvenil")
else:
  print("Mayor")
    


