## Cristian Eduardo Gonzalez Primero        65RR012     01-10-22
# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:
# ● Un constructor, donde los datos pueden estar vacíos.
# ● Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# (Edad >0, DNI Limite de 10 caracteres y opcional que valide que solo sean números)
# ● mostrar(): Muestra los datos de la persona.
# ● esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre = '', edad = int(), DNI = ''):
        self.nombre = nombre
        self.edad = self._is_valid_age(edad)
        self.dni = self._is_valid_dni(DNI)
    
    # getter method
    @property
    def get_nombre(self):
        return self.nombre
    
    @get_nombre.setter
    def set_nombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    # getter method
    @property
    def get_edad(self):
        return self.edad
    
    @get_edad.setter
    def set_edad(self, nuevaEdad):
        self.edad = self._is_valid_age(nuevaEdad)

    # getter method
    @property
    def get_dni(self):
        return self.dni

    @get_dni.setter
    def set_dni(self, c):
        self.dni = self._is_valid_dni(c)

    def mostrar(self):
        print(self.nombre)
        print(self.edad)
        print(self.dni)

    def esMayorDeEdad(self):
        if self.edad >= 18:
            print('Es mayor de edad.')
            return True
        else:
            return False

    def _is_valid_age(self, age):
        if age < 0:
            raise ValueError("Edad negativa no aceptada")
        return age
    
    def _is_valid_dni(self, _dni):
        if len(_dni) > 10:
            raise ValueError("DNI no puede exceder más de 10 carácteres.")
        return _dni
