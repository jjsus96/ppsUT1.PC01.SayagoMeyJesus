tupla = (23, 23, 46, 3, 2, 54, 23, 34, 24, 64)

array = []

for i in range(1, 11):
    array.append(int(input("Escribe una edad: ")))

cantidad = 0
for elemento in array:
    if elemento >= 20:
        cantidad = cantidad + 1
    else:
        cantidad = cantidad

print(cantidad)
