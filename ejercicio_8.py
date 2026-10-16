nota = float(input("ingresa la nota (0 a 100):"))

if nota < 0 or nota > 100:
    print("Error: La nota debe estar entre o y 100")
elif nota >= 70:
    print("Estudiante aprobado")
else:
    print("Estudiante reprobado")

