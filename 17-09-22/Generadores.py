#Crear una función generadora de pares:

def pares(n):
    for numero in range(n+1):
        if numero % 2 == 0:
            yield numero

print(pares(10))
