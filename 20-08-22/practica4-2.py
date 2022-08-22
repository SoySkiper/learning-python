## Cristian Eduardo Gonzalez Primero 65RR012 20-08-22
## Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado.
#  Copia los elementos de la lista en otra lista pero en orden inverso, y
#  muestra sus elementos por la pantalla.

list = []

for contador in range(5):
    a = int(input('Ingresa un numero: '))
    list.append(a)

print('Tu lista original: ',list)
list2 = sorted(list)
print('Tu lista original: ',list2)

