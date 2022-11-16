lista = ["sa", "sfsaf", "dsfds", "idsids"]
entero = int(input("Escribe un numero: "))


def filtrar_palabras(i, j):
    k = []
    for l in i:
        if len(l) >= j:
            k.append(l)

    if len(k) == 0:
        print("Ninguna palabra :(")
    else:
        print(k)


filtrar_palabras(lista, entero)