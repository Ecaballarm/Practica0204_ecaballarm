# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra = input("Introduce una palabra: ")
palabra_alreves = palabra
palabra = list(palabra)
palabra_alreves = list(palabra_alreves)
palabra_alreves.reverse()
if palabra == palabra_alreves:
    print("Es una palabra palíndromo")
else:
    print("No es una palabra palíndromo")
