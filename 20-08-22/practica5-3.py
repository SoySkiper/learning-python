## Cristian Eduardo Gonzalez Primero 65RR012 20-08-22
## Programa que recibe el monto de un préstamo y el interés mensual, si el
#  interés es mayor al 30% lo marcara como un error ("El interés ingresado
#  es incorrecto")), sino informa el importe total.  

montoPresta = float(input('Ingresa monto de préstamo: '))
interesMes = float(input('Ingresa el interés mensual: '))
meses = int(input('Ingresa número de meses: '))

if interesMes >= 30:
    print('El interés ingresado es incorrecto')
else:
    print('Importe total: ', meses*(montoPresta * (interesMes/100)))
