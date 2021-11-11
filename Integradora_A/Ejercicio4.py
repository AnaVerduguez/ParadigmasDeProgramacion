#4)Se quiere generar el código de programación necesario para realizar la afinación de un piano. Para esto, el afinador posee un dispositivo que escucha la nota de cada tecla, la compara con una nota esperada, e indica si es correcta o no. La nota escuchada en el piano será correcta si la celda que la representa tiene el mismo color que la celda que representa la nota esperada. Hay dos tipos de teclas, blancas y negras, por lo que hay dos formas de representar la nota, con una celda blanca (vacía) o negra. En el caso contrario, el dispositivo indicará que la nota del piano debe afinarse y esto se representará marcando la nota mediante una celda de color Rojo. La siguiente imagen muestra un ejemplo antes y después de la verificación donde: 
#● Cada columna representa una tecla o nota del piano. 
#● Solo se representan las primeras 12 teclas del piano. 
#● La primer tecla (de izquierda a derecha) está afinada pues ambas notas son de color negro. 
#● La cuarta tecla también está afinada, pues ambas son de color blanco. 
#● La segunda tecla está desafinada, pues la nota del piano escuchada es de color negro, y la esperada es de color blanco. Se le pide que implemente el procedimiento VerificarAfinacionDePiano() que indica con un casillero rojo aquellas teclas del piano que deben afinarse, para un piano de 88 teclas. Antes de llamar al procedimiento Luego de llamar al procedimiento

#Primero debemos de crear una lista donde me cuarde las notas segun la imagen del enunciado
nota_piano= ["N","N","B","B","N","N","N","B","N","B","B","N"]
nota_esperada= ["N","B","N","B","B","N","B","N","B","B","N","N"]
afinacion= [] 

print("Bienvenido al afinador de piano")
print("Debe de tener en cuenta que solo existen dos teclas, blancas(B) y negras(N). En caso de que se necesite afinacion se marcara con una celda en rojo(R) ")

#Creo mi funcion aplicando un ciclo for p in range con parametros del 0 al 12 que permite saber si la nota_piano y la nota_esperada son iguales, en caso de que no lo sea(quiere decir que esta desafinada) se acumula una R en la lista afinacion.
def VerificarAfinacionDePiano():
  #12 filas del piano
  for p in range (0,12):
    nota= nota_piano[p]
    esperada= nota_esperada[p]

    if nota != esperada:
      afinacion.append("R")
    else:
      afinacion.append("B")
    nota = ""
    esperada= ""
  print(afinacion)

print("NOTA PIANO:")
print(nota_piano)

print("NOTA ESPERADA:")
print(nota_esperada)

print("LUEGO DE LLAMAR AL PROCEDIMIENTO")
VerificarAfinacionDePiano()

