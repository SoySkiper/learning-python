def div(a,b):
    try:
        return a/b
    except:
        print("No se puede dividir entre 0")
    finally:
        #También se ejecuta
        print("Entra a finally")

def div2(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
