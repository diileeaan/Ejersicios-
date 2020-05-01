texto = input("Introduzca el texto: ").lower()

vocales = ('a', 'e', 'i', 'o', 'u')

for letra in vocales:
    texto = texto.replace(letra, "")
print(texto)