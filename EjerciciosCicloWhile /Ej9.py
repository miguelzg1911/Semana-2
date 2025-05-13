# Sumar hasta detenerse:
# Pide números al usuario y súmalos hasta que ingrese "0", momento en el que se imprimirá el total.

suma = 0
while True:
    numeros = float(input("Ingresa tus numeros: "))
    if numeros == 0:
        break
    suma += numeros
print(suma)
