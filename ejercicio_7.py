edad = (input("Ingresa tu edad: "))

if edad < 0:
    print("ERROR, la edad no puede ser negativa")
elif edad >= 18:
    print("puedes ingresar al evento")
else:
    print("No puedes ingresar el evento")
    