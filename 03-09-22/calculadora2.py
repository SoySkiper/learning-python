
primerNumero = input(int('Ingresa el primer numero: '))
segundoNumero = input(int('Ingresa el segundo numero: '))

Calculadora(primerNumero, segundoNumero)

class Calculadora:
    def __init__ (self, num1, num2):
        print('Calculadora.')
        self.num1 = num1
        self.num2 = num2
        self.validarCero()
        self.calcular()

    @property
    def listaNum1(self):
        return self.num1
    @listaNum1.setter
    def listaNum1(self, nuevoNumero1):
        self.num2 = input(int('Ingresa valor 1:'))

    @property
    def listaNum2(self):
        return self.num2
    
    @listaNum2.setter
    def listaNum2(self, nuevoNumero2):
        self.num2 = input(int('Ingresa valor 2:'))


    
    def validarCero(self):
        if self.num2 == 0:
            print('No se puede realizar esta operación')

    def calcular(self):
            suma = self.num1 + self.num2
            resta = self.num1 - self.num2
            multiplicacion = self.num1 * self.num2
            division = self.num1 / self.num2
            print('La suma es: ', suma)
            print('La resta es: ', resta)
            print('La multiplicación es: ', multiplicacion)
            print('La división es: ', division)
