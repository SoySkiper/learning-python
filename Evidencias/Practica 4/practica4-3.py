## Cristian Eduardo Gonzalez Primero 65RR012 20-08-22
## Se quiere realizar un programa que lea por teclado las 5 notas obtenidas
#  por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar
#  todas las notas, la nota media, la nota más alta que ha sacado y la menor.


listaNotas = []
i = 0

while i <= 4:
    nota = int(input('Ingresa tu nota: '))
    if nota >=0 and nota <=10:
        listaNotas.append(nota)
    else:
        print('Ingresa correctamente el valor entre 0 y 10')
        i -= 1
    i += 1

print('Las notas son: ', listaNotas)
print('Nota media: ', (sum(listaNotas))/5)
print('Nota más alta: ', max(listaNotas))
print('Nota más baja: ', min(listaNotas))
