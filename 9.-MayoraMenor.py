lista = []
n = int(input("¿Cuantos numeros agregaras?:"))
for i in range(n):
	valor=int(input("Ingrese numero %i: "%(i+1)))
	lista.insert(i,valor)
print ("Los numeros que agregaste son: ",lista)

lista.sort()

lista.reverse()

print("Estos son los números en orden de mayor a menor : ", lista)