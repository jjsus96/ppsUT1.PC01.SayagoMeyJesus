nota = int(input("Proporcione un valor entre 0 y 10: "))

if 10 >= nota >= 9:
    print("A")
elif 9 > nota >= 8:
    print("B")
elif 8 > nota >= 7:
    print("C")
elif 7 > nota >= 6:
    print("D")
elif 6 > nota >= 0:
    print("F")
elif ValueError:
    print("Introduzca un valor entre 0 y 10")