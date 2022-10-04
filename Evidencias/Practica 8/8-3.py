## Cristian Eduardo Gonzalez Primero    65RR012     17-09-22

#Vamos a crear un programa en python donde vamos a declarar un diccionario
#para guardar los precios de las distintas frutas. El programa pedirá el
#nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio
#final de la fruta a partir de los datos guardados en el diccionario.
#Si la fruta no existe nos dará un error. Tras cada consulta el programa nos
#preguntará si queremos hacer otra consulta.

# def informacion(d):
#     fruta = input("Ingresa una fruta vendida: ")
#     cantidad = int(input("Ingresa cantidad: "))
#     try:
#         d[fruta]
#         precio = (d[fruta])*cantidad
#         print(precioF)
#     except:
#         print("Error: La fruta no está registrada")

def repetir(repeat):
    if repeat == 'y':
        return True
    elif repeat == 'n':
        return False

def cantidadValida(cDF):
    try:
        resp = int(cDF)
        if resp == '':
            print('¡Tu respuesta es correcta!\n')
        else:
            print('Respuesta incorrecta, la respuesta correcta es ', '\n')
    except:
        print('Respuesta invalida \n')

diccionarioDeFrutas = {"manzana": 35, "mango": 40, "piña": 40, "plátano": 18, "naranja": 10, "jicama": 15, "fresa": 35, "aguacate": 45, "pera": 25}

i = True
while i == True:
    #Aqui inicia programa
    print('Lista de Frutas: ')
    for itemListaFrutas in diccionarioDeFrutas:
    frutaVendida = input('Fruta vendida: ')
    try:
        cantidadDeFruta = int(input('Cantidad: '))
    except ValueError:
        print('La cantidad es numérico')
    # while type(cantidadDeFruta) != 
    print('Pasaste la prueba')

    #Aquí termina y confirma repetir programa
    rep = input('¿Quieres hacer otra consulta? (y/n) ')
    i = repetir(rep)
    while i == None:
        rep = input('¿Quieres hacer otra consulta? (y/n) ')
        i = repetir(rep)