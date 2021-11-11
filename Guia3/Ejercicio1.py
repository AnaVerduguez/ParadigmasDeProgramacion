#1)Informar los primeros 100 números naturales y su sumatoria

#Defino a la variable sumatoria en 0, para que empiece el conteo desde ahi
sumatoria= 0

#Aplico un parametro para que el programa me imprima por pantalla numeros naturales del 1 al 100 
for i in range (1,101):
  print(i)
  sumatoria = sumatoria+i

print("La sumatoria de los primeros 100 numeros naturales es:" ,sumatoria)