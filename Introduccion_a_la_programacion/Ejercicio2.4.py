caracter = input("Introduzca un caracter: ")
vocales = ["a", "e", "i", "o", "u"]


def cuentavocales(caracter):
    if caracter in vocales:
        print("true")
        return True
    else:
        print("false")
        return False


cuentavocales(caracter)