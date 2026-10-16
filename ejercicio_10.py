usuario_correcto = "admin"
contraseña_correcta = "1234"

usuario = input("ingresa tu usuario: ")
contraseña = input("ingresa tu contraseña: ")

if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("Acceso permitido,bienvenido")
else:
    print("usuario o contraseña incorrectos")