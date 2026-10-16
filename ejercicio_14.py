saldo = 500000

while True:
    print("CAJERO AUTOMATICO BANCOLOMBIA")
    print("1. consultar saldo")
    print("2. retirar dinero")
    print("3. depositar dinero")
    print("4. salir")

    opcion = input("selecciona una opcion: ")

    if opcion == "1":
        print("Tu saldo actual es:",saldo)
    elif opcion == "2":
        retiro = float(input("cuanto deseas retirar?: "))
        if retiro <= 0:
            print("error: el retiro debe ser mayor a 0")
        elif retiro > saldo:
            print("error: no tiene suficiente saldo")
        else:
            saldo = saldo - retiro
            print("retiro exitoso")
            print("saldo restante: $", saldo)

    elif opcion == "3":
        deposito = float(input("Cuanto dinero vas a depositar?: "))
        if deposito <= 0:
            print("Error: el deposito debe ser mayor a 0.")
        else:
            saldo = saldo + deposito
            print("El deposito a sido exitoso")
            print("Tu saldo actual es de: $",saldo )
    elif opcion == "4":
        print("Gracias por utilizar nuestros servicios, gracias.")
        break
    else:
        print("Opcion no validad, elija otra opcion.")

