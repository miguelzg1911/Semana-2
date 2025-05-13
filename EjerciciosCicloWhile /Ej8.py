# Validar contraseña:
# Pide al usuario una contraseña y usa un while para seguir pidiendo hasta que ingrese "python123".

contraseña = "python123"
while True:
    palabra = input("Ingresa una contraseña: ")
    if palabra == contraseña:
        print("Contraseña Correcta")
        break
    else:
        print("Ingresa la contraseña correcta")
