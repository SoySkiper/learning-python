class Acuatico:
    def __init__(self, nombre, edad):
        self.nombre = ''
        self.edad = 0
    def nadar(self):
        print('El animal acuatico nada')


#tiburon = acuatico('Max', 2)
#tiburon.nadar()

class Terrestre:
    def __init__(self, nombre, tamano):
        self.nombre = ''
        self.tamano = ''
    def caminar(self):
        print(self.nombre, ' camina con el tamaño de ', self.tamano)


class reptil(Acuatico, Terrestre):
    def __init__(self, nombre, producto, tamano):
        self.nombre = nombre
        self.producto = producto
        self.tamano = tamano
    def vender(self):
        print('Se puede crear ', self.producto)


#cocodrilo = reptil('Cocodrilo', 'cinturon', '3m')
#cocodrilo.nadar()
#cocodrilo.caminar()
#cocodrilo.vender()
