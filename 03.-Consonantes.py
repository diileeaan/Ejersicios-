Vocales = ("a","e","i","o","u", " ")
texto = input("Ingresar el texto: ")
texto_nuevo = 0
for letters in texto:
    if letters not in Vocales:
        texto_nuevo = texto_nuevo + 1
print("El numero de consonantes es: ", texto_nuevo)