## Obtener la suma de todos los elementos en la lista
# lista = [1,2,3,4]

def repetir(repeat):
    if repeat == 'y':
        return True
    elif repeat == 'n':
        return False

r = True
while r == True:
    lista = [1,2,3,4]

    for i in  lista:
        for j in lista:
            print(i, ' + ', j , ' = ', i+j)

    rep = input('¿Intentar de nuevo? (y/n) ')
    r = repetir(rep)
    while r == None:
        rep = input('¿Intentar de nuevo? (y/n) ')
        r = repetir(rep)