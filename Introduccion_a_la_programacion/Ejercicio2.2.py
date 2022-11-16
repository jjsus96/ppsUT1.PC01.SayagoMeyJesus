valor1 = float(input("Introduzca el primer número: "))
valor2 = float(input("Introduzca el segundo número: "))
valor3 = float(input("Introduzca el segundo número: "))

def max_de_tres(i, j, k):
    if k < i > j:
        print("El número mayor es", i)
    elif i < j > k:
        print("El número mayor es", j)
    elif j < k > i:
        print("El número mayor es", k)
    else:
        print("Los números introducidos son iguales")


max_de_tres(valor1, valor2, valor3)