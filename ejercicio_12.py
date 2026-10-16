print("Hola, ingresa las medidas de los 3 lados de un triangulo")
lado1 = float(input("Ingresa el primer lado del triangulo: "))
lado2 = float(input("Ingresa el segundo lado del triangulo: "))
lado3 = float(input("Ingresa el tercer lado del triangulo: "))

if lado1 < 0 or lado2 < 0 or lado3 < 0:
    print("Error: los lados deben ser mayores a 0.")
elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("el triangulo no es valido")
elif lado1 == lado2 and lado2 == lado3:
    print("el triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("el triangulo es isosceles")
else:
    print("el triangulo es escaleno")
