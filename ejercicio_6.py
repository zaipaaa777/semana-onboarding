numero1 = float(input("Bienvenido, ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
operacion = input("ingresa la operacion que quieres hacer(+,-,*,/): ")
if operacion == "+":
    resultado = numero1 + numero2
    print("resultado: ", resultado)
elif operacion == "-":
    resultado = numero1 - numero2
    print("resultado: ", resultado)
elif operacion == "*":
    resultado = numero1 * numero2
    print("resultado: ",resultado)
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("resultado: ",resultado)
    else:
        print("ERROR: No se puede dividir entre 0.")
else: 
    print("Operacion no valida")
    