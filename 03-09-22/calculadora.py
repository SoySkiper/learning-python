class Calculadora:
    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.menu()
        self.salirPrincipal = ''

    def menu():
    ##salirPrincipal = ''
    while salirPrincipal != 'Salir':
        print('''Calculadora
            1. Suman
            2. Resta
            3. Multiplicación
            4. División
            5. Salir''')
        option = input(str('Selecciona una opción: '))
        salir = ''
        if option == '1':
            print('Ingresa')
            while salir != 'Salir':
                self.num1 = input(int('Ingresa valor 1: '))
                self.num2 = input(int('Ingresa valor 2: '))
                print(self.num1 * self. num2)
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
