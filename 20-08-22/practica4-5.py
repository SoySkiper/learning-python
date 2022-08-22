## Cristian Eduardo Gonzalez Primero 65RR012 20-08-22
## Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido.
#  Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres
#  de los alumnos y los valores serán listados con las notas de cada alumno.
## El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos
#  un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
#  Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

dicAlumnos = {}
numAlumnos = int(input('Ingresa el número de alumnos: '))
i = 0
if numAlumnos > 0 and i < numAlumnos:
    for contador in range(numAlumnos):
        nuevoAlumnoNom = str(input('Ingresa el nombre del alumno: '))
        nuevaCalif = int(input('Ingresa sus notas, termina ingresando numero negativo(-): '))
        if(nuevaCalf => 0)
            califAlumno = []
            califAlumno.append(nuevaCalif)
            dicAlumnos[nuevoAlumnoNom] = califAlumno

#hola = 'Hola mundo'
#i = 90
#dicAlumnos[hola] = i
#print(dicAlumnos)
