## Cristian Eduardo Gonzalez Primero  65RR012   16/08/22
## Programa que genera patrones de asteriscos


arrAstetic = ['*', '*', '*']
arrNoAstetic = ['*']
end = ' '
astetic = '*'
salto = '\n'

## Ejercicio 1:
def ejercicio1 (arrAs):
    ## Solución en cadena
    for indice in arrAs:
        print(' '.join(arrAs))

    print(salto)

    ## Ejercicio (otra manera que se me ocurrió):
    for contador in range(3):
        print(arrNoAstetic*3) 


## Ejercicio 2:
def ejercicio2 (a):
    for contador in range(3):
        print(' '.join(a))
        escalera = a.append(astetic)

    del a[0:3]
    print(salto)

    ## Solución en lista
    for contador in range(3):
        print(a)
        escalera = a.append(astetic)


## Ejercicio 3:
def ejercicio3 (arrA):
    for contador in range(3):
        print(arrA)
        longitud = len(arrA) - 1
        del arrA[longitud]
        longitud -= 1
    
    arrA.extend(['*', '*', '*'])
    print(salto)

    for contador in range(3):
        print(' '.join(arrA))
        longitud = len(arrA) - 1
        del arrA[longitud]
        longitud -= 1


## Ejercicio 4:
def ejercicio4 (listAstetic):
    for contador in range(3):
        print(listAstetic)
        longitud = len(listAstetic) - 1
        del listAstetic[longitud]
        listAstetic.insert(contador, end)
        longitud -= 1

    del listAstetic[0:3]
    listAstetic.extend(['*', '*', '*'])
    print(salto)

    for contador in range(3):
        print(' '.join(listAstetic))
        longitud = len(listAstetic) - 1
        del listAstetic[longitud]
        listAstetic.insert(contador, end)
        longitud -= 1


print('Ejercicio 1:' + salto)
ejercicio1(arrAstetic)
print(salto + 'Ejercicio 2:' + salto)
ejercicio2(arrNoAstetic)
print(salto + 'Ejercicio 3:' + salto)
ejercicio3(arrAstetic)
print(salto + 'Ejercicio 4:' + salto)
## Reinicio variable 
arrAstetic.extend(['*', '*', '*'])
ejercicio4(arrAstetic)