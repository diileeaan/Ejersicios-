archivo = open("palabra.txt", "a")
palabra = input("Escriba una palabra: ")
archivo.write(palabra + "\n")
archivo.close()
