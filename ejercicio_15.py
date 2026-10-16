nombre = input("ingresa el nombre del cliente: ")
producto = input("ingresa el nombre del producto: ")
precio = float(input("ingresa el precio del producto: "))
cantidad = int(input("ingresa la cantidad: "))

if precio <= 0 or cantidad <=0:
    print("Error: el precio y la cantidad de producto deben ser mayor a 0")
else:
    subtotal = precio * cantidad

    if subtotal >= 500000:
        descuento = subtotal * 0.15
    elif subtotal >= 200000:
        descuento = subtotal * 0.10
    else:
        descuento = 0

    total = subtotal - descuento

    print("FACTURA DE COMPRA")
    print("cliente: ",nombre)
    print("producto: ",producto)
    print("precio unitario: ",precio)
    print("cantidad: ",cantidad)
    print("subtotal: ",subtotal)
    print("descuento: ",descuento)
    print("total a pagar: ",total)
