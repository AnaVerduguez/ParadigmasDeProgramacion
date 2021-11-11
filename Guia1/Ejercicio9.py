#Escribir un programa que utilice la función anterior para generar una tabla de conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10. 

#Toma los parametros del 0 al 120 dando saltos de 10 en 10
for i in range (0,121,10):
  #Utilizo la funcion round para redondear mi resultado
  #Aplico la formula que nos permite convertir de °F a °C
  print(i ,"°F" ,"=" ,round((i - 32) * 5/9) ,"°C") 

