lista1 = [3, 5, 7, 9]
lista2 = [1, 2, 3, 4]


def superposicion(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False


print(superposicion(lista1, lista2))