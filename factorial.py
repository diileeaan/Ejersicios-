#Factorial: se denomina factorial o factorial de n al producto de todos los números naturales desde 1 hasta n.

número= int(input("Ingresa un número por favor: "))

def factorial(n):
    if n == 0 or n == 1:
        valor = 1
    elif n > 1:
        valor = n * factorial (n-1)
    return valor

print ("El resultado es: ",factorial(número))



        