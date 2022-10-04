## Cristian Eduardo Gonzalez Primero    65RR012     27-08-22

##Una persona adquirió un producto para pagar en 20 meses.
#El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente.
#Realizar un algoritmo para determinar cuánto debe pagar mensualmente y
#el total de lo que pagó después de los 20 meses.

meses = 20
primerPago = 10

for i in range(meses):
    print('En el mes ', i+1, ' se paga ', primerPago)
    primerPago += primerPago
