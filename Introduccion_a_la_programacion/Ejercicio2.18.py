year = int(input("Introduzca un año para saber si es o no bisiesto: "))


def es_bisiesto(i):
    prueba1 = i % 4
    prueba2 = i % 100
    prueba3 = i % 400
    if prueba1 == 0 and prueba2 != 0 or (prueba2 != 0 and prueba3 == 0):
        print("Es Bisiesto")
    else:
        print("No es Bisiesto")


es_bisiesto(year)