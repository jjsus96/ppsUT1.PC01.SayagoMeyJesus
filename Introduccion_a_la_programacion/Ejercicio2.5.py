lista = [1, 2, 3, 4]


def sumar(lista):
    contarsum = 0
    for i in lista:
        contarsum += i
    print(contarsum)


def multiplicar(lista):
    contarmult = 1
    for i in lista:
        contarmult *= i
    print(contarmult)

sumar(lista)
multiplicar(lista)