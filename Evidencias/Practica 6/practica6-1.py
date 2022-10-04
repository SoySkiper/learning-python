## Cristian Eduardo Gonzalez Primero    65RR012     27-08-22

##Realizar un ejemplo de menú, donde podemos escoger las distintas opciones
#hasta que seleccionamos la opción de “Salir”.

#ejemplo: 
#Menú de recomendaciones
#   1. Literatura
#   2. Cine
#   3. Música
#   4. Videojuegos
#   5. Salir

def menu():
    salirPrincipal = ''
    while salirPrincipal != 'Salir':
        print('''Menú de recomendaciones
            1. Literatura
            2. Cine
            3. Música
            4. Videojuegos
            5. Salir''')
        option = input(str('Selecciona una opción: '))
        salir = ''
        if option == '1':
            print('Seleccionaste literatura, ¿Qué quieres leer?')
            while salir != 'Salir':
                salir = input(str('Escribe "Salir" para regresar al menú principal: '))
        elif option == '2':
            print('Seleccionaste cine, ¿Qué película quieres ver?')
            while salir != 'Salir':
                salir = input(str('Escribe "Salir" para regresar al menú principal: '))
        elif option == '3':
            print('Seleccionaste Música, ¿Qué quieres escuchar?')
            while salir != 'Salir':
                salir = input(str('Escribe "Salir" para regresar al menú principal: '))
        elif option == '4':
            print('Seleccionaste Videojuegos, ¿Qué quieres jugar?')
            while salir != 'Salir':
                salir = input(str('Escribe "Salir" para regresar al menú principal: '))
        elif option == '5':
            salirPrincipal == 'Salir'
            break
        else:
            print('Selecciona la opción correcta.')
menu()
