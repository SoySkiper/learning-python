## Cristian Eduardo Gonzalez Primero        65RR012     01-10-22

##Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
# ● Un constructor, donde los datos pueden estar vacíos.
# ● Los setters y getters para cada uno de los atributos. El atributo no se puede
# modificar directamente, sólo ingresando o retirando dinero.
# ● mostrar(): Muestra los datos de la cuenta.
# ● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad
# introducida es negativa, no se hará nada.
# ● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar
# en números rojos.

class Cuenta:
    def __init__(self, titular, cantidad=float()):
        self.titular = titular
        self.cantidad = cantidad

    @property
    def get_titular(self):
        return self.titular
    
    @get_titular.setter
    def set_titular(self, nuevoTitular):
        self.titular = nuevoTitular

    @property
    def get_cantidad(self):
        return self.cantidad
    
    def mostrar(self):
        print('Titular: ',self.titular)
        print('Cantidad: ',self.cantidad)

    def ingresar(self, ingreso):
        if ingreso >= 0:
            self.cantidad += ingreso
            return self.cantidad
        else:
            return self.cantidad
            
    def retirar(self, retiro):
        self.cantidad -= retiro
        return self.cantidad
