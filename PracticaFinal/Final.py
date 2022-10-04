#Cristian Eduardo Gonzalez Primero      65RR012         24-09-22
import imgAhorcado
import palabras
import random
import copa

#Fución para repetir juego
def jugarDeNuevo():
    # Esta función devuelve True si ingresa la letra "s", de lo contrario termina ejecución
    print('¿Quieres jugar de nuevo? (s)')
    return input().lower().startswith('s')

# Esta funcion retorna la palabra para adivinar.
def buscarPalabraAleat(arrPalabras):
    palabraParaAdivinar = random.randint(0, len(arrPalabras)-1)
    return arrPalabras[palabraParaAdivinar]

#Función que muetra ahorcado de manera grafica y respuestas
def mostrarTablero(arrAhorcado, letrasIncorrecta, letrasCorrecta, palabraSecreta):
    print("¡Adivina la palabra!")
    print(arrAhorcado[len(letrasIncorrecta)],'\n')
    print('Letras incorrectas: ')
    for letra in letrasIncorrecta:
        print(letra, end=' ')
    print("")
    espaciosVacíos = '_' * len(palabraSecreta)
    # Completar los espacios vacíos con las letras adivinadas
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrecta:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]
    # mostrar la palabra secreta con espacios entre cada letra
    for letra in espaciosVacíos:
        print(letra, end=' ')
    print("")

def obtenerIntento(letrasProbadas):
    # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
    while True:
        print('Ingresa una letra: ')
        intento = input()
        intento = intento.lower()
        # Compronbamos la entrada del ususario con los posibles fallos.
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento

arrPalabras = palabras.palabras
arrAhorcado = imgAhorcado.arrAhorcado
letraCorrecta = ""
letraIncorrecta = ""
juegoTerminado = False
adivinarEstaPalabra = buscarPalabraAleat(arrPalabras)
win = copa.copa

while True:
    #Inicio de juego
    mostrarTablero(arrAhorcado, letraIncorrecta, letraCorrecta, adivinarEstaPalabra)
    intento = obtenerIntento(letraIncorrecta + letraCorrecta)
    if intento in adivinarEstaPalabra:
        # Incorpora los intentos a la cadena posible
        letraCorrecta = letraCorrecta + intento
        # Verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(adivinarEstaPalabra)):
            if adivinarEstaPalabra[i] not in letraCorrecta:
                encontradoTodasLasLetras = False
                break

        if encontradoTodasLasLetras:
            print('\n¡La palabra secreta es "' + adivinarEstaPalabra.upper() + '"! ¡Has ganado!\n')
            print(win)
            juegoTerminado = True
    else:
        letraIncorrecta = letraIncorrecta + intento
        # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letraIncorrecta) == len(arrAhorcado) - 1:
            mostrarTablero(arrAhorcado, letraIncorrecta, letraCorrecta, adivinarEstaPalabra)
            print('Perdiste, la palabra era "' + adivinarEstaPalabra + '"')
            juegoTerminado = True

    #Fin de jeugo
    if juegoTerminado:
        if jugarDeNuevo():
            # Se reinician variables cada vez que se inicia el juego
            letraIncorrecta = ""
            letraCorrecta = ""
            juegoTerminado = False
            adivinarEstaPalabra = buscarPalabraAleat(arrPalabras)
        else:
            break