#Cristian Eduardo Gonzalez Primero

from math import sqrt

entradaPrimos = int(input('¿Cuántos números primos quieres imprimir? '))

def esPrimo(n):
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def generaPrimos(n):
    for i in filter(esPrimo, range(3,n+1,2)):
        yield i
print(2)

for i in generaPrimos(entradaPrimos):
 print(i)

#Mostrar en pantalla los N primero número primos.
#Se pide por teclado la cantidad de números primos que queremos mostrar.

nP = int(input('¿Cuántos números primos quieres mostrar?'))

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

def listaPrimo(numPrimo, es_primo):
    arrPrimo = []
    i=2
    while len(arrPrimo) < numPrimo:
        if es_primo(i) == True:
            arrPrimo.append(i)
        i+=1
    print(arrPrimo)

listaPrimo(nP, es_primo)

