# Adivina el número :
# Genera un número secreto (puedes usar una variable fija)
# y usa un while para pedirle al usuario que lo adivine. Da pistas si el número es mayor o menor.

NUMERO = 8

while True:
    numero = int(input("Ingresa un numero del 1 al 15: "))
    if numero >= 1 and numero <= 4:
        print("Nuuuu, estas abajo")
    elif numero >=5 and numero <= 7:
        print("Ya te vas acercando")
    elif numero == 8:
        print("Felicidades, has encontrado el numero")
        break
    elif numero > 8 and numero <= 10:
        print("Ya casi lo tienes")
    elif numero > 10 and numero < 15:
        print("Ya estas muy arriba")
    else:
        print("Ingresa un numero en el rango del 1 al 15")