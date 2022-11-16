cadena = input("Introduzca una frase para invertirla: ")


def inversa(cadena):
    inversion = ""
    for i in cadena:
        inversion = i + inversion
    print(inversion)
    return inversion


inversa(cadena)
