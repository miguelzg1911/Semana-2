# Número de intentos:
# Pide al usuario que ingrese un número entre 1 y 10. Si no lo hace, sigue pidiéndolo hasta que lo haga correctamente.

while True:
    numeros = int(input("Ingresa un numero: "))
    if numeros < 1 or numeros > 10:
        print("Siguelo intentando")
        continue
    else:
        print("Lo encontraste")
    break

