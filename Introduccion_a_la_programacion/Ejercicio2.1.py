valor1 = float(input("Introduzca el primer número: "))
valor2 = float(input("Introduzca el segundo número: "))


def customax(i, j):
    if i > j:
        print(i, "Es mayor que", j)
    elif j < i:
        print(j, "Es mayor que", i)
    else:
        print(j, "Es igual", i)


customax(valor1, valor2)
