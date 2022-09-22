def decorador(fun):
    def funcion():
        print('Esto es un decorador 1')
        f = fun()
        print('Esto es un decorador 2')
        return f
    return funcion

@decorador
def hola():
    print('Hola mundo')

hola()
