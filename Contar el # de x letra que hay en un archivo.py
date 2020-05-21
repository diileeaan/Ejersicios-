
archivo = open("palabra.txt","r")
texto = archivo.read()

contarletra = 0

for letra in texto:
    if letra == 'a':
        contarletra += 1
    
print ("hay: ", contarletra, "a")