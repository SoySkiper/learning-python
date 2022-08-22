## Cristian Eduardo Gonzalez Primero 65RR012 20-08-22
## Crea una tupla con los meses del año, pide números al usuario, si el número
#  está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa
#  posición sino muestra un mensaje de error. El programa termina cuando el
#  usuario introduce un cero.

tuplaMeses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

mes = 1

while mes != 0:
    mes = int(input('Ingresa el numero de mes (1-12)\n Con 0 terminas el programa: '))
    if(mes > 0 and mes <= 12):
        mes -= 1
        print(tuplaMeses[mes])
        mes += 1
    elif(mes > 12 and mes < 0):
        print('Error')
        
print('Programa terminado')
