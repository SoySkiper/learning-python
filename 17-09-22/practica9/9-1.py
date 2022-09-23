#Cristian Eduardo Gonzalez Primero      65RR012

##Realice un programa que pregunte aleatoriamente una multiplicación. 
# El programa debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea incorrecta 
# el programa debe indicar cuál es la correcta). El programa preguntará 10 multiplicaciones, y al finalizar 
# mostrará el número de aciertos.

import random

def numeroValido(rU, rC):
    try:
        resp = int(rU)
        if resp == rC:
            print('¡Tu respuesta es correcta!\n')
        else:
            print('Respuesta incorrecta, la respuesta correcta es ', rC, '\n')
    except:
        print('Respuesta invalida \n')

def repetirMultiplicación(repeat):
    if repeat == 'y':
        return True
    elif repeat == 'n':
        return False

i = True
while i == True:
    primerNumero = random.randint(0, 10)
    segundoNumero = random.randint(0,10)
    respuestaCorrecta = primerNumero * segundoNumero

    print('¿Puedes resolver la siguiente multiplicación?')
    print(primerNumero, ' x ', segundoNumero)
    respuestaUsuario = input('Respuesta: ')
    numeroValido(respuestaUsuario, respuestaCorrecta)

    repetir = input('¿Intentar de nuevo? (y/n) ')
    i = repetirMultiplicación(repetir)

    while i == None:
        repetir = input('¿Intentar de nuevo? (y/n) ')
        i = repetirMultiplicación(repetir)
