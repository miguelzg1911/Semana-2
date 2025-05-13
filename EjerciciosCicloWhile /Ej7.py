
palabra = input("Ingresa una palabra: ").lower()

vocales = "aeiou"

i = 0
contador = 0

while i < len(palabra):
    if palabra[i] in vocales:
        contador += 1
    i += 1

print(f"La palabra tiene {contador} vocal/es")
