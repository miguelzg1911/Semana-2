# Solicitar número positivo :
# Pide al usuario un número y usa un while para seguir pidiendo hasta que ingrese un número positivo.

while True:
    numero = int(input("Ingresa un numero positivo: "))
    if numero <= 0:
        print("Invalido. Ingresa un numero positivo")
    else:
        print("El numero positivo que ingresaste fue:",numero)
        break