#Cristian Eduardo Gonzalez Primero      65RR012

##Obtener el cuadrado de todos los elementos en la lista.
# Lista: 1,2,3,4,5,6,7,8,9,10

def repetir(repeat):
    if repeat == 'y':
        return True
    elif repeat == 'n':
        return False

i = True
while i == True:

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Cuadrado de los elementos de la lista: ', lista)
    for value in lista:
        print(value**2)
    
    rep = input('¿Intentar de nuevo? (y/n) ')
    i = repetir(rep)
    while i == None:
        rep = input('¿Intentar de nuevo? (y/n) ')
        i = repetir(rep)
