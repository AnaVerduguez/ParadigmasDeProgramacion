#14 crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
#•	Las cantidades totales de cada artículo.
#•	La cantidad de artículos en la sucursal 2.
#•	La cantidad del artículo 3 en la sucursal 1.
#•	La recaudación total de cada sucursal.
#•	La recaudación total de la empresa.
#•	La sucursal de mayor recaudación.

#Primero creo mis listas que voy a utilizar
precios= []
cantidades_vendidadas= []

#Aplicamos un ciclo que me permita ingresar la cantidad de articulos, esto lo hacemos con un for i in range. Tambien pedimos lo mismo per ocon la cantidad de articulos.
for i in range(0,5):
  precios.append(float(input("Ingrese el precio del articulo{0}: ".format((i+1)))))

for r in range(0,4):
  cantidades_articulos= []
  for q in range(0,5):
    cantidades_articulos.append(int(input("Ingrese la cantidad de articulos en la sucursal:{0} ".format(q+1,r+1))))
    cantidades_vendidadas.append(cantidades_articulos)

#Luego de pedir los datos de entrada debo de realizar las operaciones para los articulos
# Para eso debo crear otra lista donde vayan sumados todos los totales por cada sucursal
total_sucursal = []
for cantidad_sucursal in cantidades_vendidadas:
    total=0
    for precios,cantidades_vendidadas in zip(precios,cantidad_sucursal):
        total=total+precios*cantidades_vendidadas
    total_sucursal.append(total)

#Para saber el maximo aplico otro bucle que me permite establecer las veces que se repite en este caso 4 veces ya que son 4 sucursales
max_recaudacion = max(total_sucursal)   
p = 1
for p in range(4):
    print("Las recaudaciones de la sucursal {0} son: {1}".format(p+1,total_sucursal[p]))
    p = p + 1

print("Recaudacion total de la empresa: {0}".format(sum(total_sucursal)))
print("Sucursal de mayor recaudacion : {0}".format(p))


