import pathlib
import time
import os

dirRaiz = 'ascii/'
arrDogBeer = []
directorio = pathlib.Path(dirRaiz)

for fichero in directorio.iterdir():
    ficheroDirectorio = str("ascii/" + fichero.name)
    arrDogBeer.append(ficheroDirectorio)
arrDogBeer.sort()

i = 0
while True:

    txtDogBeer1 = open(arrDogBeer[i % len(arrDogBeer)], 'r')
    dogBeer1 = txtDogBeer1.read()
    print(dogBeer1)
    txtDogBeer1.close()
    
    time.sleep(.1)
    i += 1
    # for windows OS
    if os.name =="nt":
        os.system("cls")
		
	# for linux / Mac OS
    else:
        os.system("clear")