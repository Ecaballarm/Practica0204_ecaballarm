# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
# y muestre por pantalla el menor y el mayor de los precios.

precios = [50, 75, 46, 22, 80, 65, 8]
menor = mayor = precios[0]
for precio in precios:
    if precio < menor:
        menor = precio
    if precio > mayor:
        mayor = precio
print("El precio más barato es " + str(menor))
print("El precio más caro es " + str(mayor))
