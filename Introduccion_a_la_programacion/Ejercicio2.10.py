lista = [0, 7, 3, 1, 8, 5, 6, 3, 2, 4]


def max_in_list(i):
    k = i[0]

    for j in i:
        if k <= j:
            k = j
        else:
            k = k
    print(k)


max_in_list(lista)
