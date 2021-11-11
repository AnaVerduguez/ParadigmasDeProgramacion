#15. Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:
#•	Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
#•	Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna
#de la tabla anterior, y en la segunda los goles del otro equipo.
#El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
#¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?

#Primero creo mi lista

equipos=[]
resultados=[]

#Aplico un ciclo que me permite ingresar los datos por teclado a mis listas
for i in range(0,15):
  partido=[]
  #Ingreso los nombres de los participantes
  partido.append(input("Ingrese el nombre del equipo 1 del partido{0}: ".format(i+1)))
  partido.append(input("Ingrese el nombre del equipo 2 del partido{0}:".format(i+1)))
  equipos.append(partido)
  goles=[]
  #Ingreso los goles que metio cada participante
  goles.append(int(input("Ingrese los goles del primer equipo: {0}".format(partido[0]))))
  goles.append(int(input("Ingrese los goles del segundo equipo: {0}".format(partido[1]))))
  resultados.append(goles)

print("BIENVENIDO")
print("Los resultados son:")
#Imprimo por pantalla los resultados
for partido,goles in zip(equipos,resultados):
    if goles[0] > goles [1]:
        print("El equipo 1 gano")
    else:
        if goles[0] < goles [1]:
            print("El equipo 2 gano")
        else:
            print("Hubo un empate")

