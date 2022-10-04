#Cristian Eduardo Gonzalez Primero      65RR012     17-09-22

#Escribe un programa python que pida un número por teclado y que cree un
#diccionario cuyas claves sean desde el número 1 hasta el número indicado,
#y los valores sean los cuadrados de las claves.

def anadirClaves(nC,dic):
    for i in range(1, nC+1):
        raiz = i**2
        dic[i] = raiz

def principal():
    dictionary = {}
    numClaves = 0
    while numClaves >= 0:
        try:
            numClaves = int(input("""Valor negativo para terminar

Ingresa número de claves para diccionario: """))

            anadirClaves(numClaves, dictionary)
            print(dictionary)
            dictionary = {}
        except:
            print("Ingresa valor entero")

principal()
