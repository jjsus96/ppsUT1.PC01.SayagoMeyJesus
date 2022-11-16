numbinario = str(input("Introduzca un numero binario:"))


def calcbin(num):
    res = 0
    for i in range(len(num)):
        res += int(num[i]) * 2 ** (len(num) - i - 1)
    print(res)

calcbin(numbinario)


print(" ")
curso = int(input("Proporciona el año actual:"))

nombre1 = str(input("Proporciona el nombre de la persona1:"))
nacim1 = int(input("Proporciona el año de nacimiento de la persona1:"))

nombre2 = str(input("Proporciona el nombre de la persona2:"))
nacim2 = int(input("Proporciona el año de nacimiento de la persona2:"))

nombre3 = str(input("Proporciona el nombre de la persona3:"))
nacim3 = int(input("Proporciona el año de nacimiento de la persona3:"))

edad1 = curso - nacim1
edad2 = curso - nacim2
edad3 = curso - nacim3

print(nombre1, "tiene", edad1)
print(nombre2, "tiene", edad2)
print(nombre3, "tiene", edad3)