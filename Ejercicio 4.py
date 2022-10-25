# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

ganador = []

for premiado in range(3):
    premiado = int(input("Los numeros ganadores son: "))
    ganador.append(premiado)

ganador.sort()

print("Los números ganadores, de menor a mayor orden, son: " + str(ganador))