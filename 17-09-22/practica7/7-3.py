## Obtener la cantidad de elementos mayores a 5 en la tupla.
# tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)

def repetir(repeat):
    if repeat == 'y':
        return True
    elif repeat == 'n':
        return False

i = True
while i == True:
    tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)

    for valor in  tupla:
        if valor > 5:
            print(valor)

    rep = input('¿Intentar de nuevo? (y/n) ')
    i = repetir(rep)
    while i == None:
        rep = input('¿Intentar de nuevo? (y/n) ')
        i = repetir(rep)