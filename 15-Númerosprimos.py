lista = []
suma = 0
for i in range(10):
    num = int(input("Ingrese el numero %i: "%(i+1)))
    if (num != 1 ):
        if (num == 2 or num == 3 or num == 5 or num == 7 or num == 11):
            lista.insert(i,num)
        else:
            operacion = num % 2 
            if (operacion != 0):
                if num%3:
                    if num%5:
                        if num%7:
                            if num%11:
                                lista.insert(i,num)
    print("Los numeros primos son: ", lista)




