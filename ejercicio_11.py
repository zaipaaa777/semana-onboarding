temperatura = float(input("ingresa la temperatura en °c"))
if temperatura < 10:
    print("El dia es frio")
elif temperatura < 25:
    print(" El dia es templado")
elif temperatura < 35:
    print("El dia es caluroso")
else:
    print("El dia es muy caluroso")