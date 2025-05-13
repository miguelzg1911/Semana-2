# Menú interactivo :
# Crea un menú con while que permite al usuario elegir entre opciones 
# (por ejemplo, "1. Saludar", "2. Despedirse", "3. Salir") 
# y solo termina cuando elige la opción de salir.

while True:
    print("\n""1. Saludar")
    print("2. Despedirse")
    print("3. Salir")

    opcion = input("\n""Elige una opcion (1-3): ")
    if opcion == "1":
        print("Saludar")
    elif opcion == "2":
        print("Despedirse")
    elif opcion == "3":
        print("Salir")
        break
    else:
        print("Elige una opcion valida")