lista = [8.5, 9.2, 7.8, 6.9, 9.7, 8.1, 7.5, 10.0, 8.8, 6.5, 9.0, 7.2, 8.6, 9.5, 7.9]
n = len(lista)
swapped = True
while swapped:
    swapped = False
    for i in range(n - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            swapped = True
print("Orden Asendente:", lista)
n = len(lista)
swapped = True
while swapped:
    swapped = False
    for i in range(n - 1):
        if lista[i] < lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            swapped = True             
print("Orden Desendente:", lista)