import numpy as np
#Definicion de matrices
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
#Suma alemento a elemento
suma = A+B
print("..SUMA(A+B)..")
print(suma)
#Multiplicacion
prod_elem= A*B
print("..Multiplicacion(AXB)..")
print(prod_elem)
#Producto MATRICAL
prod_mat=A@B
print("..Producto matricial(A@B)..")
#Transpuesta
transpuesta = A.T
print("..Transpuesta de A.T ..")
print(transpuesta)
#Determinante e inversa
det=np.linalg.det(A)
inv=np.linalg.det(B)
print("..Determinante de A..")
print(det)
print("..Determinante de B..")
print(inv)