#Cristian Eduardo Gonzalez Primero      65RR012     17-09-22

#Escribe un programa que lea una cadena y devuelva un diccionario
#con la cantidad de apariciones de cada carácter en la cadena.

def principal():
    cadena = "0"
    while cadena != "":
        cadena = str(input("""Deja vacio para terminar
Ingresa una cadena de texto: """))
        if cadena != "":
            leerCadena(cadena)

def leerCadena(c):
    dictionary = {}
    for letter in c:
        contadorLetras = c.count(letter)
        if contadorLetras > 0:
            dictionary[letter] = contadorLetras
    print(dictionary)
    
principal()
