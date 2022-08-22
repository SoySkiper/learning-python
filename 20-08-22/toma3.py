## toma3.py
## Cristian Eduardo Gonzalez Primero

arr = ['*', '*', '*']
arrS = ['*']

for contador in range(3):
	print(arr)
	if(contador<2):
		del arr[contador]

print('\n')

for contador in range(3):
	print(arrS*contador)
	