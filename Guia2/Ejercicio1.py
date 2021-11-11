#1)A partir de dos valores enteros A y B, informar la suma, la diferencia (A menos B), y el producto.
#Estrategia:
#Solicitar e ingresar datos por teclado
#Calcular suma e informar por monitor
#Calcular diferencia e informar por monitor
#Calcular producto e informar por monitor

#Se pide por teclado el valor de A y B
valor_a=int(input("Ingrese el valor de A:"))
valor_b=int(input("Ingrese el valor de B:"))

#Operaciones a realizar:
suma= valor_a + valor_b
diferencia= valor_a - valor_b
producto= valor_a * valor_b

#Se imprime por pantalla el resultado de las operaciones
print("La suma entre" ,valor_a ,"y" ,valor_b ,"es:" ,suma)
print("La diferencia entre" ,valor_a ,"y" ,valor_b ,"es:" ,diferencia)
print("El producto entre" ,valor_a ,"y" ,valor_b ,"es:" ,producto)
