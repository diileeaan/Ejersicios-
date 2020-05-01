lista = []
n = int(input("¿Cuantos numeros agregaras?:"))
for i in range(n):
	valor= float(input("Ingrese numero %i: "%(i+1)))
	lista.insert(i,valor)
print ("Los numeros que agregaste son: ",lista)
lista.sort()
print("Estos son los números en orden de Menor a Mayor : ", lista)
y = (lista[-1])
entero = round(y)
print("El mayor numero fue", entero)
if entero == 10:
	print("Diez")
if entero == 9:
	print("Nueve")
if entero == 8:
	print("Ocho")
if entero == 7:
	print("Siete")
if entero == 6:
	print("Seis")
if entero == 5:
	print("Cinco")
if entero == 4:
	print("Cuatro")
if entero == 3:
	print("Tres")
if entero == 2:
	print("Dos")
if entero == 1:
	print("Uno")