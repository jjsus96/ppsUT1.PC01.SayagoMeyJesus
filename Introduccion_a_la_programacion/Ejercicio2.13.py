cadena = str(input("Introduzca una cadena:"))


def numayus(i):
    cont = 0
    for j in i:
        if j == j.upper():
            cont += 1
    print("El numero de mayusculas es:", cont)


numayus(cadena)