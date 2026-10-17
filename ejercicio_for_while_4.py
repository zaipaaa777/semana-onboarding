texto = input("ingresa un texto: ")
vocales = 0

for letra in texto:
    if letra in "aeiouAEIOU":
        vocales = vocales + 1
print("el texto tiene:", vocales ,"vocales")
