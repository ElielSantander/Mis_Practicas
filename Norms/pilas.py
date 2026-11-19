lista =[]
for i in range (1,11):
    lista.append(i)
Nolista=lista[-1]
print(Nolista)

for _ in range(4):
    lista.pop()
print(lista)

elementos_rest=len(lista)
print("Los elementos restantes son: ", elementos_rest)

pilaencero=len(lista)==0
print("El historial es: ",pilaencero)
