print("MENU DE OPERACIONES")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")


num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

opcion = input("seleciona una opcion entre 1-4: ")

if opcion == "1":
    resultado = num1 + num2
    print("El resultado de la suma es: ",resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("El resultado de la resta es: ",resultado)
elif opcion == "3":
    resultado = num1 * num2
    print("El resultado de la multiplicacion es: ",resultado)
elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la division es: ",resultado)
    else:
        print("Error: No se puede dividir entre 0.")
else:
    print("Opcion no valida")