import math
lista = []
suma = 0
n = int(input("¿Cuantos numeros agregaras?:"))
for i in range(n):
    valor = int(input("Ingrese el numero %i: "%(i+1)))
    lista.insert(i,valor)
    suma = suma+valor
moda = []
valorInicial = lista.count(lista[0])
for i in range(10):
    var = lista[i]
    valorRepetitivo = lista.count(var)
    if(valorRepetitivo > valorInicial):
        valorInicial = valorRepetitivo
        moda = []
        moda.insert(0,var)
    elif(valorRepetitivo == valorInicial and var not in moda):
        valorInicial = valorRepetitivo
        moda.insert(i,var)
print("La moda es: ",moda)
x= suma/10
print("La media es :",x)
vari = (lista[i]-x)**2
varia = vari/9
print (math.sqrt(varia))


