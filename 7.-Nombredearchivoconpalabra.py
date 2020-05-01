archivo = open(input("Ingresa el nombre del archivo con extencion(Ejemplo: palabra.txt): "), "a")
palabra = input("Escriba una palabra: ")
archivo.write(palabra + "\n")
archivo.close()
