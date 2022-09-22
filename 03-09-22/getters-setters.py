class Humano:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.valEdad()

    @property
    def listaNombre (self):
        return self.nombre

    @listaNombre.setter
    def listaNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    @property
    def listaEdad(self):
        return self.edad

    @listaEdad.setter
    def listaEdad(self, nuevaEdad):
        self.edad = nuevaEdad
        self.valEdad()

    def valEdad(self):
        if self.edad >=18:
            print('Es mayor de Edad.', self.edad)
        else:
            self.edad = 0
            print('La edad es incorrecta, vuelve a ingresarla.')

