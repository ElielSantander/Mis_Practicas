import numpy as np
A = np.array([[10, 15],[20, 5]])
B = np.array([[5, 12],[15, 8]])
ventas = A + B
ingreso = ventas * 50
print("Total de productos vendidos (sabado y domingo)")
print(ventas)
print("Ingreso total en pesos (a 50 pesos por producto)")
print(ingreso)