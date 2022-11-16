lista = ["Hola1", "Holaaaaa5", "Holaaaaaaaaaaaaaaaaa17"]


def mas_larga(i):
    j = len(i[0])
    k = i[0]

    for palabra in lista:
        if j <= len(palabra):
            k = palabra
            j = len(palabra)
        else:
            k = k

    print(k)


mas_larga(lista)
