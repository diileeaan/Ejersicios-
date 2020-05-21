
lista = [10,300,2,55,1,99,8,6,90,20]

for i in range(len(lista)-1):
    for x in range(len(lista)-1):

        if lista[x] > lista[x+1]:

            temporal = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = temporal

print(lista)            