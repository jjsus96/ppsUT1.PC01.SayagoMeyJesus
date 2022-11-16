palabra = input("Introduzca una palabra: ")
vocales = ["a", "e", "i", "o", "u"]


def contar_vocales(i):
    contador = 0
    numerito = 0
    for j in i:
        if j in vocales:
            numerito+=1
            contador=+numerito
    print(contador)


contar_vocales(palabra)