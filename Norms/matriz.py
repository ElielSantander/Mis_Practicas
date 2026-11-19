#creacion de matriz
matriz=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
#Acceso a elementos
print(matriz[1][2]) #imprime indice 1 columna 

#Modificar elemento
matriz[0][0]=50

#Recorrer la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento,end=" ")
    print()
