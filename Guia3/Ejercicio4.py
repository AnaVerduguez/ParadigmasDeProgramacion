#4)En un torneo de fútbol participan K equipos. El torneo se juega con el sistema de todos contra todos. Por cada partido disputado por un equipo se dispone de la siguiente información :
#a)Nro. de equipo,
#b)Código del resultado ('P'= Perdido, 'E'= Empatado, 'G'= Ganado).
#Se arma un lote de datos con todos los resultados del torneo, agrupados por Nro. de equipo.
#Desarrollar el programa que imprima:
#1) Por cada equipo, su número y el puntaje total que obtuvo (suma 3 si gana, y 1 si empata).
#2) Nro. de equipo que totalizó la menor cantidad de puntos. (hay solo uno)

cantidad_equipos= int(input("Ingrese la cantidad de equipos que participaran del torneo:"))

contador= 0
contador_empatados= 0
contador_ganados= 0

while contador < cantidad_equipos:
 numero_equipo= int(input("Ingrese el numero del equipo:"))
 partidos_ganados= int(input("Ingrese sus partidos ganados:"))
 partidos_empatados= int(input("Ingrese sus partidos empatados:"))
 partidos_perdidos= int(input("Ingrese sus partidos perdidos:"))

 if partidos_empatados >= 1:
   contador_empatados= contador_empatados +1
 elif partidos_ganados >= 1:
   contador_ganados= contador_ganados +3

 puntos_totales= contador_empatados + contador_ganados

print("PLANILLA:")
print("El equipo N°" ,numero_equipo ,"obtuvo un puntaje total de:" ,puntos_totales)