A = ([[10, 15],[20, 5]])
B = ([[5, 12],[15, 8]])
suma = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
ingresos = [[suma[i][j] * 50 for j in range(2)] for i in range(2)]
print("Total de productos vendidos (sabado y domingo)")
print(suma)
print("Ingreso total en pesos (a 50 pesos por producto)")
print(ingresos)
