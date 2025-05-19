#1.Crea una lista llamada mi_lista con los números del 1 al 5. Ejemplo1
Mi_Lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#2.Crea una lista [10, 20, 30, 40] y muestra el primer y el último elemento.
print("(Segundo)")
Numeros = [10, 20, 30, 40]
print(Numeros[0] ,Numeros[3])

#3.A partir de [10, 20, 30, 40, 50], obtén:

#     Los elementos del índice 1 al 3.
#     Los primeros 3 elementos.
#     Los elementos desde el índice 2 hasta el final.
print("\n""(Tercero)")
Numeros1 = [10, 20, 30, 40, 50]
Nuevo_Numeros1 = Numeros1[1:3]
print(Nuevo_Numeros1)
Nuevo_Numeros2 = Numeros1[:3]
print(Nuevo_Numeros2)
Nuevo_Numeros3 = Numeros1[1:]
print(Nuevo_Numeros3)

#4.Cambia el tercer elemento de [10, 20, 30, 40] por 99.
print("\n""(Cuarto)")
Numeros2 = [10, 20, 30, 40]
Numeros2
print(Numeros2)

#5.A una lista [10, 20, 30] agrega:

#     El número 40 al final.
#     El número 15 en la posición 1.
#     Los números 50 y 60 al final de la lista.
print("\n""(Quinto)")
Numeros3 = [10, 20, 30]
print(Numeros3)
Numeros3.insert(3, 40)
print(Numeros3)
Numeros3.insert(1, 15)
print(Numeros3)
Numeros3.insert(5, 50)
print(Numeros3)
Numeros3.insert(6, 60)
print(Numeros3)

#6.De la lista [10, 20, 30, 40, 50], realiza las siguientes acciones:

#     Elimina el número 30.
#     Elimina el último elemento.
#     Elimina el segundo elemento (índice 1).
print("\n""(Sexto)")
Numeros4 = [10, 20, 30, 40, 50]
print(Numeros4)
Numeros4.remove(30)
print(Numeros4)
Eliminado = Numeros4.pop(3)
print(Numeros4)
Eliminado2 = Numeros4.pop(1)
print(Numeros4)

#7.Con la lista [10, 20, 30, 40, 50]:

#     Verifica si el número 20 está en la lista.
#     Encuentra el índice del número 30.
#     Cuenta cuántas veces aparece el número 20.
print("\n""(Septimo)")
Numeros5 = [10, 20, 30, 40, 50]

if 20 in Numeros5:
    print("El numero 20 si esta en la lista")
else:
    print("El numero 20 no esta en la lista")

Indice_de_30 = Numeros5.index(30)
print(f"El indice de 30 es: {Indice_de_30}")

Num20 = Numeros5.count(20)
print(f"El numero 20 aparece {Num20} vez/veces")

#8.Ordena la lista [40, 10, 30, 20]:

#     Primero en orden ascendente.
#     Luego en orden descendente.
#     Crea una nueva lista ordenada sin modificar la original.
print("\n""(Octavo)")
Numeros6 = [40, 10, 30, 20]
Numeros6.sort()
print(Numeros6)
Numeros6.sort(reverse=True)
print(Numeros6)
ListaNueva = sorted(Numeros6)
print(Numeros6)
print(ListaNueva)

#9.Invierte el orden de [10, 20, 30, 40] utilizando ambas técnicas.
print("\n""(Noveno)")
Numeros7 = [10, 20, 30, 40]
Invertida = Numeros7[::-1]
print("Lista original:", Numeros7)
print("Lista invertida con slicing:",Invertida)
Numeros7.reverse()
print("Lista original invertida con reverse():", Numeros7)

#10.Copia la lista [10, 20, 30] de tres maneras diferentes.
print("\n""(Decimo)")
Numeros8 = [10, 20, 30]
Copia_Slicing = Numeros8[:]
print("Lista principal:",Numeros8)
print("Lista copiada con slicing:",Copia_Slicing)

Copia_List = list(Numeros8)
print("Lista principal:",Numeros8)
print("Lista copiada con list:",Copia_List)

Copia_Copy = Numeros8.copy()
print("Lista principal:",Numeros8)
print("Lista copiada con copy:",Copia_Copy)

#11.Crea una lista vacía y escribe un código que imprima "La lista está vacía" si no contiene datos.
print("\n""(Onceavo)")
Lista_Vacia = []

if len(Lista_Vacia) == 0:
    print("Esta lista esta vacia")
else:
    print("Esta lista tiene", len(Lista_Vacia), "elementos")

#12.Escribe un programa que:

#     Pregunte al usuario cuántos elementos quiere ingresar.
#     Luego pida esos elementos uno por uno.
#     Finalmente, muestre la lista completa.
print("\n""(Doceavo)")
NumeroDatos = int(input("Cuantos datos quieres ingresar?: "))
Lista = []

for i in range(NumeroDatos):
    CadaDato = input(f"Ingresa el dato que desees {i+1}: ")
    Lista.append(CadaDato)
print("Estos son los datos ingresados:",Lista)

