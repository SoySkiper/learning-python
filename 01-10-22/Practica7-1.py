## Cristian Eduardo Gonzalez Primero        65RR012         01-10-22

# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:
# ● Un constructor, donde los datos pueden estar vacíos.
# ● Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# (Edad >0, DNI Limite de 10 caracteres y opcional que valide que solo sean números)
# ● mostrar(): Muestra los datos de la persona.
# ● esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.


class Persona:
    def __init__(self, nombre, edad = int(), dni):
        self.nombre = nombre
        self.edad = edad
        self.dni