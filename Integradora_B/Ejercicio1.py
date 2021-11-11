#1) Se desarrolla una carrera automovilística de regularidad constituida por 50 trayectos numerados de 1 a 50. Por cada trayecto se registra  el número de trayecto y el tiempo asignado en segundos y se encuentran en el archivo ASIGNADO (sin ningún orden)
#a) Nro. del trayecto	b) Tiempo asignado en segundos (4 dígitos)
#Para llevar el control de los corredores, de posición y de abandonos se dispone de un archivo TIEMPO donde cada registro contiene:
#a) Nro. del corredor (3 dígitos)	b) Nro. del trayecto	c) Tiempo en segundos (4 dígitos)

#El lote esta ordenado por trayecto pero no por corredor. A partir del abandono de un corredor en un trayecto no habrá más ingresos en el lote.
#Desarrollar estrategia, algoritmo y codificación del programa que determine e imprima:
#1) Por cada etapa, su número y el del corredor ganador de la misma.
#2) Por cada etapa, su número y los de los corredores que abandonan en la misma.

#Esto me permite generar numeros aleatorios para el tiempo y el numero de corredor en vez de ingresarlos por teclado
import random 
#Primero comenzamos definiendo nuestras listas
tiempo_trayecto= []
corredores_total= []
corredores_ganadores= []
corredores_abandonaron= []

#Luego creo mis funciones en donde aplicare mis listas mas adelante
def carrera (tiempo,corredores,ganador,abandono):
  j= 0
  #Definimos que son 50 trayectos
  trayectos_totales= 50
  
  for j in range(0,51):
    trayectos_totales= trayectos_totales - 1
    j= j + 1
    print("RECORRIDO N° " + str(j) + ":")
    #Defino mi tiempo y el corredor de forma aleatoria
    segundos = [random.randint (1000,9999)]
    print("El tiempo en segundos es: ", segundos)   
    #Agrego el tiempo a mi lista
    tiempo_trayecto.append(segundos)
    corredor = [random.randint (100,999)]
    print("El numero del corredor es:" ,corredor)
    #Agrego el numero del corredor a mi lista
    corredores_total.append(corredor)

    abandono= input("El corredor abandono la carrera? SI O NO :").upper()
    if abandono == "SI":
      corredores_abandonaron.append(corredor)

carrera (tiempo_trayecto, corredores_total,corredores_ganadores,corredores_abandonaron)


print("RESULTADOS:")
print("El ganador de la etapa es :",corredores_ganadores)
print("Los conductores que abandonaron fueron: ",corredores_abandonaron)


