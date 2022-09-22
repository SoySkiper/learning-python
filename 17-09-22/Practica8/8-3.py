## Cristian Eduardo Gonzalez Primero    65RR012     17-09-22

#Vamos a crear un programa en python donde vamos a declarar un diccionario
#para guardar los precios de las distintas frutas. El programa pedirá el
#nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio
#final de la fruta a partir de los datos guardados en el diccionario.
#Si la fruta no existe nos dará un error. Tras cada consulta el programa nos
#preguntará si queremos hacer otra consulta.


def principal():
    dicc = {"manzana": 35, "mango": 40, "piña": 40, "plátano": 18, "naranja": 10, "jicama": 15, "fresa": 35, "aguacate": 45, "pera": 25}
    n = ""
    while n == "":
        informacion(dicc)

def informacion(d):
    fruta = input("Ingresa una fruta vendida: ")
    cantidad = int(input("Ingresa cantidad: "))
    try:
        d[fruta]
        precio = (d[fruta])*cantidad
        print(precioF)
    except:
        print("Error: La fruta no está registrada")

principal()
