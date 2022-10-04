## Cristian Eduardo Gonzalez Primero 65RR012 20-08-22
## Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido.
#  Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres
#  de los alumnos y los valores serán listados con las notas de cada alumno.
## El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos
#  un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
#  Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

dicAlumnos = {}
numAlumnos = int(input('Ingresa el número de alumnos: '))

for cantidad in range(numAlumnos):
    alumno = str(input('Introduce el nombre del alumno: '))

    while alumno in dicAlumnos:
        print('Alumno ya registrado.')
        alumno = str(input('Introduce el nombre del alumno: '))

    calificaciones = []
    nota = float(input('Introduce una nota (numero negativo para terminar): '))

    while nota >= 0:
        calificaciones.append(nota)
        nota = float(input('Introduce una nota (numero negativo para terminar): '))

    dicAlumnos[alumno] = calificaciones.copy()

for alumno, calificaciones in dicAlumnos.items():
    print(alumno, ' ha sacado de nota media ',"{0:.2f}".format(sum(calificaciones)/len(calificaciones)))