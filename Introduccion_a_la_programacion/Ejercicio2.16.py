nombres = []


for i in range(1, 10):
    nombres.append(input("Escribe un nombre: ").lower())
buscar = input("Qué letra buscas?: ")
cantidad = 0


for nombre in nombres:
    for letra in nombre:
        if letra == buscar:
            cantidad = cantidad + 1
            break
        else:
            cantidad = cantidad


print(cantidad)
