precio = float(input("Ingresa el precio de la compra: "))

if precio < 0:
    print("error: el precio no puede ser negativo")
elif precio >= 200000:
    descuento = precio * 0.20
    total = precio - descuento
    print("A recibido descuento del 20%, el total a pagar es de: ", total)
elif precio >= 100000:
    descuento = precio * 0.10
    total = precio - descuento
    print("A recibido descuento del 10%, el total a pagar es de: ", total)
else:
    print("El total a pagar es de: ",precio)