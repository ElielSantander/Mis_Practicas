from collections import deque
cola=deque()
#Agregar elementos a la cola(encolar)
cola.append("cliente 1")
cola.append("cliente 2")
cola.append("cliente 3")
#Sacar el primer elemento que llego (desencolar)
atendida=cola.popleft()
#Mostrar rswusltados obtenidos
print("Atenndido:",atendida)
print("cola restante",cola)


