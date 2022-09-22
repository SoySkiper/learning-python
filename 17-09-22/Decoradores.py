def decorador(fun):
    print('Esto es un decorador')
    return fun

@decorador
def hola():
    print('Hola Mundo')

hola()
