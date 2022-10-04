## Cristian Eduardo Gonzalez Primero 65RR012 20-08-22
## Realizar un programa que inicialice una lista con 10 valores aleatorios 
#  (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista 
#  junto con su cuadrado y su cubo.

import random

list = []

for contador in range(0, 10):
    list.append(random.randint(1,10))
    print(list)

i = 0
for valor in list:
    print('Numero de la lista: ', list[i], ' Cuadrado ', list[i]**2, ' Cubo ', list[i]**3 )
    i+=1
